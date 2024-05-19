import logging
from settings import BOT, ADMIN_CHAT_ID

logging.basicConfig(filename='log.log', filemode='w', level=logging.ERROR)

class MyLogsHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            BOT.send_message(text=log_entry, chat_id=ADMIN_CHAT_ID,)
        except Exception as e:
            logging.error(e)
