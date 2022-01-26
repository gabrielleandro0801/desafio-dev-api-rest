from datetime import datetime
from typing import List

from flask_sqlalchemy import BaseQuery, Pagination
from src.domain.models.transactions import Transactions, TransactionTypes
from src.infrastructure.database.connection.db_connection import db, paginated_result, get_pagination_limit_and_page


class TransactionsRepository:

    @classmethod
    def save(cls, transaction: Transactions) -> None:
        db.session.add(transaction)
        db.session.commit()

    @classmethod
    def get_withdraws_of_the_day(cls, account_id: int) -> List[Transactions]:
        query: BaseQuery = Transactions.query.filter(Transactions.account_id == account_id,
                                                     Transactions.type == TransactionTypes.WITHDRAW,
                                                     Transactions.date >= datetime.now().strftime('%Y-%m-%d'))
        transactions = query.all()
        db.session.commit()
        return transactions

    @classmethod
    def get_transactions_from_period(cls, account_id: int, **kwargs) -> dict:
        query: BaseQuery = Transactions.query.filter(Transactions.account_id == account_id)

        if kwargs.get("from") is not None:
            query = query.filter(Transactions.date >= kwargs.get("from"))

        if kwargs.get("to") is not None:
            query = query.filter(Transactions.date <= kwargs.get("to"))

        page, limit = get_pagination_limit_and_page(kwargs.get("page"), kwargs.get("limit"))
        transactions: Pagination = query.paginate(page=page, error_out=False, max_per_page=limit)

        response: dict = paginated_result(Transactions, transactions, limit)
        db.session.commit()
        return response
