from environs import Env
import requests
import telegram
import logging


def get_reviews(token, timestamp=None):
    response = requests.get(url='https://dvmn.org/api/long_polling/', headers={'Authorization': f'Token {token}'},
                            params={'timestamp': str(timestamp)})
    response.raise_for_status()
    reviews = response.json()
    return reviews


if __name__ == '__main__':
    logging.basicConfig(filename="log.log", level=logging.INFO)
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str('TELEGRAM_BOT_TOKEN'))
    timestamp = None
    while True:
        try:
            reviews = get_reviews(env.str('DEVMAN_TOKEN'), timestamp)
            if reviews['status'] == 'found':
                for attempt in reviews['new_attempts']:
                    text = f'У вас проверили работу [«{attempt["lesson_title"]}»]({attempt["lesson_url"]})\n'
                    text += 'К сожалению, в работе есть ошибки.' if attempt['is_negative'] \
                        else 'Преподавателю все понравилось, можно ладить дальше.'
                    bot.send_message(text=text, chat_id=env.str('TELEGRAM_CHAT_ID'), parse_mode='Markdown')
            if "timestamp_to_request" in reviews:
                timestamp = reviews['timestamp_to_request']
            else:
                timestamp = reviews['last_attempt_timestamp']
        except requests.exceptions.ReadTimeout as e:
            logging.error("Timeout error: %s", e)
        except requests.exceptions.ConnectionError as e:
            logging.error("Connection error: %s", e)
