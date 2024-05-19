import logging
from settings import BOT, ADMIN_CHAT_ID




class MyLogsHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        BOT.send_message(text=log_entry, chat_id=ADMIN_CHAT_ID,)