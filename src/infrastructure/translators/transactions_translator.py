from typing import Any


class TransactionsTranslator:

    @classmethod
    def get_operation_type(cls, operation: str) -> Any:
        from src.domain.models.transactions import TransactionTypes
        from src.domain.services.transactions_service import DepositService
        from src.infrastructure.database.repositories.transactions_repository import TransactionsRepository

        options: dict = {
            TransactionTypes.DEPOSIT: DepositService(
                transactions_repository=TransactionsRepository
            ),
            # TransactionTypes.WITHDRAW: withdraw_service
        }
        return options.get(operation)

    @classmethod
    def translate_transaction_from_body(cls, body: dict):
        from datetime import datetime
        import src.domain.models.transactions as t

        return t.Transactions(
            value=body.get('amount'),
            type=body.get('operationType'),
            date=datetime.now(),
            account_id=body.get('accountId')
        )
