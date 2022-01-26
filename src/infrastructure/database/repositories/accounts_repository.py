from typing import List
from flask_sqlalchemy import BaseQuery

from src.domain.models.accounts import Accounts
from src.infrastructure.database.connection.db_connection import db


class AccountsRepository:

    @classmethod
    def find_by_user_id_and_status(cls, user_id: int, status: List[str]) -> Accounts or None:
        query: BaseQuery = Accounts.query.filter(Accounts.user_id == user_id, Accounts.status.in_(status))
        account = query.first()
        db.session.commit()
        return account

    @classmethod
    def create_account(cls, account: Accounts) -> Accounts:
        db.session.add(account)
        db.session.commit()
        return account

    @classmethod
    def find_by_account_id(cls, account_id: int) -> Accounts or None:
        query: BaseQuery = Accounts.query.filter(Accounts.id == account_id)
        account = query.first()
        db.session.commit()
        return account

    @classmethod
    def close_account(cls, account: Accounts) -> None:
        db.session.delete(account)
        db.session.commit()

    @classmethod
    def update_status(cls, account: Accounts, status: str) -> None:
        db.session.query(Accounts).filter(Accounts.id == account.id).update({Accounts.status: status})
        db.session.commit()

    @classmethod
    def update_balance(cls, account: Accounts, current_balance: float):
        db.session.query(Accounts).filter(Accounts.id == account.id).update({Accounts.balance: current_balance})
        db.session.commit()
