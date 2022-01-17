from src.infrastructure.database.connection.db_connection import db, Base


class Accounts(Base):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    value = db.Column(db.Float)
    date = db.Column(db.Datetime)
    account_id = db.Column(db.Integer)
