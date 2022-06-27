from api.infrastructure.database.connection.db_connection import db


class AccountStatus:
    ACTIVE = 'ACTIVE'
    LOCKED = 'LOCKED'
    CLOSED = 'CLOSED'


EXISTING_ACCOUNT_STATUS = [
    AccountStatus.ACTIVE,
    AccountStatus.LOCKED
]


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column('id', db.Integer, primary_key=True)
    status = db.Column('status', db.String(6), nullable=False)
    number = db.Column('number', db.Integer, nullable=False)
    bank_branch = db.Column('bank_branch', db.String(4), nullable=False)
    balance = db.Column('balance', db.Float, nullable=False)
    withdraw_daily_limit = db.Column('withdraw_daily_limit', db.Float, nullable=False)
    user_id = db.Column('user_id', db.Integer, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.status = kwargs.get('status')
        self.number = kwargs.get('number')
        self.bank_branch = kwargs.get('bank_branch')
        self.balance = kwargs.get('balance')
        self.withdraw_daily_limit = kwargs.get('withdraw_daily_limit')
        self.user_id = kwargs.get('user_id')

    def is_able_to_do_transaction(self) -> bool:
        return self.status == AccountStatus.ACTIVE

    def is_able_to_lock(self) -> bool:
        return self.status == AccountStatus.ACTIVE

    def is_able_to_unlock(self) -> bool:
        return self.status == AccountStatus.LOCKED

    def is_able_to_close(self) -> bool:
        return self.status == AccountStatus.ACTIVE

    def is_able_to_list_transactions(self) -> bool:
        return self.status in [AccountStatus.ACTIVE, AccountStatus.LOCKED]
