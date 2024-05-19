import telegram
from environs import Env

env = Env()
env.read_env()

BOT = telegram.Bot(token=env.str('TELEGRAM_BOT_TOKEN'))
DEVMAN_TOKEN = env.str('DEVMAN_TOKEN')
ADMIN_CHAT_ID = env.str('TELEGRAM_CHAT_ID')