from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta

HOST = 'localhost'
PORT = 5432
USER = 'postgres'
PASSWORD = 'password'
DATABASE = 'postgres'
DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

db = SQLAlchemy()

Base: DeclarativeMeta = declarative_base()


def start_connection(app: Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app=app)
