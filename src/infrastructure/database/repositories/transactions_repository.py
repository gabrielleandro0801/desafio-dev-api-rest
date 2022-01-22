from datetime import datetime

from flask_sqlalchemy import BaseQuery

import src.domain.models.transactions as t
from src.infrastructure.database.connection.db_connection import db


class TransactionsRepository:

    @classmethod
    def save(cls, transaction: t.Transactions) -> None:
        db.session.add(transaction)
        db.session.commit()

    @classmethod
    def get_account_withdraws_of_the_day(cls, account_id):
        query: BaseQuery = t.Transactions.query.filter(t.Transactions.account_id == account_id,
                                                       t.Transactions.type == t.TransactionTypes.WITHDRAW,
                                                       t.Transactions.date >= datetime.now().strftime('%Y-%m-%d'))
        transactions = query.all()
        db.session.commit()
        return transactions
