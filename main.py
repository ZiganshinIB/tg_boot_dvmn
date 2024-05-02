from environs import Env
import requests
import telegram
import logging


def get_long_polling_data(token, timestamp=None):
    kwargs = {'url': 'https://dvmn.org/api/long_polling/',
              'headers': {'Authorization': f'Token {token}'}}
    if timestamp is None:
        kwargs['params'] = {'timestamp': str(timestamp)}
    response = requests.get(**kwargs)
    response.raise_for_status()
    response_long_polling = response.json()
    return response_long_polling


if __name__ == '__main__':
    logging.basicConfig(filename="log.log", level=logging.INFO)
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str('TELEGRAM_BOT_TOKEN'))
    timestamp = None
    while True:
        try:
            data_long_polling = get_long_polling_data(env.str('DEVMAN_TOKEN'), timestamp)
            if data_long_polling['status'] == 'found':
                for attempt in data_long_polling['new_attempts']:
                    text = f'У вас проверили работу [«{attempt["lesson_title"]}»]({attempt["lesson_url"]})\n'
                    text += 'К сожалению, в работе есть ошибки.' if attempt['is_negative'] \
                        else 'Преподавателю все понравилось, можно ладить дальше.'
                    bot.send_message(text=text, chat_id=env.str('TELEGRAM_CHAT_ID'), parse_mode='Markdown')
            if "timestamp_to_request" in data_long_polling:
                timestamp = data_long_polling['timestamp_to_request']
            else:
                timestamp = data_long_polling['last_attempt_timestamp']
        except requests.exceptions.ReadTimeout as e:
            logging.error("Timeout error: %s", e)
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)
