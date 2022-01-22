from typing import Any, List

import src.domain.models.transactions as t


class TransactionsTranslator:

    @classmethod
    def get_operation_type(cls, operation: str) -> Any:
        from src.domain.models.transactions import TransactionTypes
        from src.domain.services.transactions_service import DepositService
        from src.domain.services.transactions_service import WithdrawService
        from src.infrastructure.database.repositories.transactions_repository import TransactionsRepository

        options: dict = {
            TransactionTypes.DEPOSIT: DepositService(
                transactions_repository=TransactionsRepository
            ),
            TransactionTypes.WITHDRAW: WithdrawService(
                transactions_repository=TransactionsRepository,
                transactions_translator=TransactionsTranslator
            )
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

    @classmethod
    def get_sum_of_withdraws(cls, transactions: List[t.Transactions]) -> float:
        total: float = 0

        for transaction in transactions:
            total += transaction.value

        return total
