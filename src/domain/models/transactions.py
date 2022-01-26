from src.infrastructure.database.connection.db_connection import db


class TransactionTypes:
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'


class Transactions(db.Model):
    __tablename__ = "transactions"

    id = db.Column('id', db.Integer, primary_key=True)
    type = db.Column('type', db.String(8), nullable=False)
    value = db.Column('value', db.Float, nullable=False)
    date = db.Column('date', db.DateTime, nullable=False)
    account_id = db.Column('account_id', db.Integer, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.type = kwargs.get('type')
        self.value = kwargs.get('value')
        self.date = kwargs.get('date')
        self.account_id = kwargs.get('account_id')

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'value': self.value,
            'operationType': self.type
        }
