import logging
import time


class MyLogsHandler(logging.Handler):

    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record, **kwargs):
        log_entry = self.format(record)
        if record.levelname == 'CRITICAL':
            # Save log to file or database
            with open('log.log', 'a') as f:
                f.write(log_entry + '\n')
        try:
            self.bot.send_message(text=log_entry, chat_id=self.chat_id,)
        except Exception as e:
            new_record = logging.LogRecord(
                name=record.name,
                level=logging.CRITICAL,
                lineno=record.lineno,
                pathname=record.pathname,
                msg=e,
                args=e.args,
                exc_info=record.exc_info
            )
            time.sleep(5)
            self.emit(new_record)

