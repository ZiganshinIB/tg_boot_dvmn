import time
import telegram
import os
import requests
import logging
from dotenv import load_dotenv
from logger import MyLogsHandler


logger = logging.getLogger('Bot_Loger')


def get_reviews(token, timestamp=None):
    response = requests.get(url='https://dvmn.org/api/long_polling/', headers={'Authorization': f'Token {token}'},
                            params={'timestamp': str(timestamp)})
    response.raise_for_status()
    reviews = response.json()
    return reviews


if __name__ == '__main__':
    load_dotenv()
    logger.setLevel(logging.INFO)
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    devman_token = os.getenv('DEVMAN_TOKEN')
    admin_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    logger.addHandler(MyLogsHandler(bot=bot, chat_id=admin_chat_id))
    logger.info("Bot started")
    timestamp = None

    while True:
        try:
            reviews = get_reviews(devman_token, timestamp)
            if reviews['status'] == 'found':
                for attempt in reviews['new_attempts']:
                    text = f'У вас проверили работу [«{attempt["lesson_title"]}»]({attempt["lesson_url"]})\n'
                    text += 'К сожалению, в работе есть ошибки.' if attempt['is_negative'] \
                        else 'Преподавателю все понравилось, можно ладить дальше.'
                    bot.send_message(text=text, chat_id=admin_chat_id, parse_mode='Markdown')
            if "timestamp_to_request" in reviews:
                timestamp = reviews['timestamp_to_request']
            else:
                timestamp = reviews['last_attempt_timestamp']

        except requests.exceptions.ReadTimeout as e:
            logger.error(e, exc_info=True)
        except requests.exceptions.ConnectionError as e:
            time.sleep(15)
            logger.critical(e, exc_info=True)
        except Exception as e:
            logger.error(e, exc_info=True)
            time.sleep(5)
