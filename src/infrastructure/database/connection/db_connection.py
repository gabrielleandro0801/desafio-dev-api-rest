from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///infrastructure/database/connection/database.db'

db = SQLAlchemy()
# engine = create_engine('sqlite:///infrastructure/database/connection/database.db', echo=True)
#
# Session = sessionmaker(bind=engine)
# session = Session()

Base = declarative_base()


def start_connection(app: Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app)
