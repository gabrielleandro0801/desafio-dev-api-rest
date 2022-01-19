import flask as f
import flask_sqlalchemy as fsql

HOST = 'localhost'
PORT = 5432
USER = 'postgres'
PASSWORD = 'password'
DATABASE = 'postgres'
DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

db = fsql.SQLAlchemy()


def start_connection(app: f.Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app=app)
