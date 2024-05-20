import telegram
import os

BOT = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
ADMIN_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')