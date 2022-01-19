from src.infrastructure.database.connection.db_connection import db


class Accounts(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    number = db.Column(db.Integer)
    bank_branch = db.Column(db.String)
    balance = db.Column(db.Float)
    withdraw_daily_limit = db.Column(db.Float)
    user_id = db.Column(db.Integer)
