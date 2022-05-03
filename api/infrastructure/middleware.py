from flask import Flask
from flask_request_id_header.middleware import RequestID


def configure(app: Flask) -> None:
    app.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = 'FOO-'
    RequestID(app)
