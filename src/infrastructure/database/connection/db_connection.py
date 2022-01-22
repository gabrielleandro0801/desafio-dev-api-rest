import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

HOST: str = os.getenv('DB_HOST', 'localhost')
PORT: str = os.getenv('DB_PORT', '5432')
USER: str = os.getenv('DB_USER', 'postgres')
PASSWORD: str = os.getenv('DB_PASSWORD', 'password')
DATABASE: str = os.getenv('DB_DATABASE', 'postgres')

DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

db = SQLAlchemy()


def start_connection(app: Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app=app)
