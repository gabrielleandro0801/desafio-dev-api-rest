from typing import Any, List

from api.domain.models.transaction import Transaction


class TransactionTranslator:

    @classmethod
    def get_operation_type(cls, operation: str) -> Any:
        from api.domain.models.transaction import TransactionTypes
        from api.domain.services.transaction_service import DepositService
        from api.domain.services.transaction_service import WithdrawService
        from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository

        options: dict = {
            TransactionTypes.DEPOSIT: DepositService(
                transactions_repository=TransactionsRepository
            ),
            TransactionTypes.WITHDRAW: WithdrawService(
                transactions_repository=TransactionsRepository,
                transaction_translator=TransactionTranslator
            )
        }
        return options.get(operation)

    @classmethod
    def translate_transaction_from_body(cls, body: dict):
        from datetime import datetime

        return Transaction(
            value=body.get('amount'),
            type=body.get('operationType'),
            date=datetime.now(),
            account_id=body.get('accountId')
        )

    @classmethod
    def get_sum_of_withdraws(cls, transactions: List[Transaction]) -> float:
        total: float = 0

        for transaction in transactions:
            total += transaction.value

        return total
