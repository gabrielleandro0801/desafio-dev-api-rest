from src.infrastructure.database.connection.db_connection import db


class Accounts(db.Model):
    __tablename__ = "transactions"

    id = db.Column('id', db.Integer, primary_key=True)
    type = db.Column('type', db.String(8), nullable=False)
    value = db.Column('value', db.Float, nullable=False)
    date = db.Column('date', db.Datetime, nullable=False)
    account_id = db.Column('account_id', db.Integer, nullable=False)
