from typing import List
from flask_sqlalchemy import BaseQuery

from api.domain.models.account import Account
from api.infrastructure.database.connection.db_connection import db


class AccountsRepository:

    @classmethod
    def find_by_user_id_and_status(cls, user_id: int, status: List[str]) -> Account or None:
        query: BaseQuery = Account.query.filter(Account.user_id == user_id, Account.status.in_(status))
        account = query.first()
        return account

    @classmethod
    def create_account(cls, account: Account) -> Account:
        db.session.add(account)
        db.session.commit()
        return account

    @classmethod
    def find_by_account_id(cls, account_id: int) -> Account or None:
        query: BaseQuery = Account.query.filter(Account.id == account_id)
        account = query.first()
        return account

    @classmethod
    def close_account(cls, account: Account) -> None:
        db.session.delete(account)
        db.session.commit()

    @classmethod
    def update_status(cls, account: Account, status: str) -> None:
        db.session.query(Account).filter(Account.id == account.id).update({Account.status: status})
        db.session.commit()

    @classmethod
    def update_balance(cls, account: Account, current_balance: float):
        db.session.query(Account).filter(Account.id == account.id).update({Account.balance: current_balance})
        db.session.commit()
