from datetime import datetime
from typing import List

from flask_sqlalchemy import BaseQuery, Pagination
from api.domain.models.transaction import Transaction, TransactionTypes
from api.infrastructure.database.connection.db_connection import db, paginated_result, get_pagination_limit_and_page


class TransactionsRepository:

    @classmethod
    def save(cls, transaction: Transaction) -> None:
        db.session.add(transaction)
        db.session.commit()

    @classmethod
    def get_withdraws_of_the_day(cls, account_id: int) -> List[Transaction]:
        query: BaseQuery = Transaction.query.filter(Transaction.account_id == account_id,
                                                    Transaction.type == TransactionTypes.WITHDRAW,
                                                    Transaction.date >= datetime.now().strftime('%Y-%m-%d'))
        transactions = query.all()
        return transactions

    @classmethod
    def get_transactions_from_period(cls, **kwargs) -> dict:
        query: BaseQuery = Transaction.query.filter(Transaction.account_id == kwargs.get('accountId'))

        if kwargs.get("from") is not None:
            query = query.filter(Transaction.date >= kwargs.get("from"))

        if kwargs.get("to") is not None:
            query = query.filter(Transaction.date <= kwargs.get("to"))

        page, limit = get_pagination_limit_and_page(kwargs.get("page"), kwargs.get("limit"))
        transactions: Pagination = query.paginate(page=page, error_out=False, max_per_page=limit)

        response: dict = paginated_result(Transaction.to_json, transactions, limit)
        return response
