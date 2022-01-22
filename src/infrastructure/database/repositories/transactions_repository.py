import src.domain.models.transactions as t
from src.infrastructure.database.connection.db_connection import db


class TransactionsRepository:

    @classmethod
    def save(cls, transaction: t.Transactions) -> None:
        db.session.add(transaction)
        db.session.commit()
