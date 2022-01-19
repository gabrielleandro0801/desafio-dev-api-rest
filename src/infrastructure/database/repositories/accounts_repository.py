from typing import List

from flask_sqlalchemy import BaseQuery

import src.domain.models.accounts as a
from src.infrastructure.database.connection.db_connection import db


class AccountsRepository:

    @classmethod
    def find_by_user_id_and_status(cls, user_id: int, status: List[str]) -> a.Accounts or None:
        query: BaseQuery = a.Accounts.query.filter(a.Accounts.id == user_id, a.Accounts.status.in_(status))
        account = query.first()
        db.session.commit()
        return account

    @classmethod
    def create_account(cls, account: a.Accounts) -> a.Accounts:
        db.session.add(account)
        db.session.commit()
        return account
