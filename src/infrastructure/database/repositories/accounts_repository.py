from typing import List
from flask_sqlalchemy import BaseQuery

import src.domain.models.accounts as a
from src.infrastructure.database.connection.db_connection import db


class AccountsRepository:

    @classmethod
    def find_by_user_id_and_status(cls, user_id: int, status: List[str]) -> a.Accounts or None:
        query: BaseQuery = a.Accounts.query.filter(a.Accounts.user_id == user_id, a.Accounts.status.in_(status))
        account = query.first()
        db.session.commit()
        return account

    @classmethod
    def create_account(cls, account: a.Accounts) -> a.Accounts:
        db.session.add(account)
        db.session.commit()
        return account

    @classmethod
    def find_by_account_id(cls, account_id: int) -> a.Accounts or None:
        query: BaseQuery = a.Accounts.query.filter(a.Accounts.id == account_id)
        account = query.first()
        db.session.commit()
        return account

    @classmethod
    def close_account(cls, account: a.Accounts) -> None:
        db.session.delete(account)
        db.session.commit()

    @classmethod
    def update_status(cls, account: a.Accounts, status: str) -> None:
        db.session.query(a.Accounts).filter(a.Accounts.id == account.id).update({a.Accounts.status: status})
        db.session.commit()

    @classmethod
    def update_balance(cls, account: a.Accounts, current_balance: float):
        db.session.query(a.Accounts).filter(a.Accounts.id == account.id).update({a.Accounts.balance: current_balance})
        db.session.commit()
