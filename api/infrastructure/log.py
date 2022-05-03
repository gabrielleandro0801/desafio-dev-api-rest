import logging

from flask import request, has_request_context

logger = logging.getLogger('dock-api-challenge')
logger.setLevel(logging.INFO)
logger.propagate = False

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)


class CustomFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.request_id = request.environ.get("HTTP_X_REQUEST_ID") if has_request_context() else "N/A"
        record.funcName = record.funcName if record.funcName != '<module>' else 'N/A'
        return super().format(record)


formatter = CustomFormatter('{"level": "%(levelname)s", '
                            '"uuid": "%(request_id)s", '
                            '"timestamp": "%(asctime)s", '
                            '"file": "%(filename)s", '
                            '"function": "%(funcName)s", '
                            '"line": "%(lineno)s", '
                            '"msg": %(message)s}')

ch.setFormatter(formatter)
logger.addHandler(ch)
