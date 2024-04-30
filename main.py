from environs import Env
from requests import exceptions
import telegram
import time
import json

from api_dvmn import Devman

env = Env()
env.read_env()

bot = telegram.Bot(token=env.str('TELEGRAM_BOT_TOKEN'))

timestamp = None


if __name__ == '__main__':
    dvmn = Devman(env.str('DEVMAN_TOKEN'))
    while True:
        try:
            raw_data = json.loads(json.dumps(dvmn.get_long_polling(timestamp), indent=4, ensure_ascii=False))
            print(raw_data)
            if raw_data['status'] == 'found':
                for attempt in raw_data['new_attempts']:
                    text = f'У вас проверили работу [«{attempt["lesson_title"]}»]({attempt["lesson_url"]})\n'
                    if attempt['is_negative']:
                        text += 'К сожалению, в работе есть ошибки.'
                    else:
                        text += 'Преподавателю все понравилось, можно ладить дальше.'
                    bot.send_message(text=text, chat_id=env.str('TELEGRAM_CHAT_ID'), parse_mode='Markdown')
                bot.send_message(text='Преподаватель проверил работу!', chat_id=env.str('TELEGRAM_CHAT_ID'))
            if "timestamp_to_request" in raw_data:
                timestamp = raw_data['timestamp_to_request']
            else:
                timestamp = raw_data['last_attempt_timestamp']

        except exceptions.ReadTimeout as e:
            print(e)
        except exceptions.ConnectionError as e:
            print(e)
            print('Ошибка соединения. Повторная попытка через 5 секунд')
            time.sleep(5)
