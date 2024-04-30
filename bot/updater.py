from environs import Env
from telegram.ext import Updater

env = Env()
env.read_env()

class Bot(object):
    def __new__(cls, token=env.str('TELEGRAM_BOT_TOKEN')):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Bot, cls).__new__(cls)
            cls.updater = Updater(token=token, use_context=True)
        return cls.instance

    def stop(self):
        self.updater.stop()
