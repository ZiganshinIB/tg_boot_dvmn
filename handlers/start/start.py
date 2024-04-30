from bot import Bot
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

bot = Bot()
dispatcher = bot.updater.dispatcher


def start(update: Update, context: CallbackContext):
    print('Text')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
