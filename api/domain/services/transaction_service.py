from abc import ABC, abstractmethod
from typing import List

import api.domain.custom_exceptions as ce
from api.domain.models.account import Account
from api.domain.models.transaction import Transaction

from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository
from api.infrastructure.translators.transaction_translator import TransactionTranslator


class AbstractTransactionService(ABC):

    @abstractmethod
    def do(self, transaction: Transaction, account: Account) -> None:
        pass


class DepositService(AbstractTransactionService):
    def __init__(self, transactions_repository) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository

    def do(self, transaction: Transaction, _) -> None:
        self.__transactions_repository.save(transaction)


class WithdrawService(AbstractTransactionService):
    def __init__(self, transactions_repository, transaction_translator) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository
        self.__transaction_translator: TransactionTranslator = transaction_translator

    def do(self, transaction: Transaction, account: Account) -> None:
        if transaction.value > account.balance:
            raise ce.AccountHasNoEnoughBalance

        withdraws: List[Transaction] = self.__transactions_repository.get_withdraws_of_the_day(account.id)
        total: float = self.__transaction_translator.get_sum_of_withdraws(withdraws)

        if (total + transaction.value) > account.withdraw_daily_limit:
            raise ce.WithdrawSurpassesDailyLimitBalance

        self.__transactions_repository.save(transaction)


class TransactionService:
    def __init__(self, transaction_translator) -> None:
        self.__transaction_translator: TransactionTranslator = transaction_translator

    def do_transaction(self, body: dict, account: Account) -> None:
        transaction: Transaction = self.__transaction_translator.translate_transaction_from_body(body)

        service: AbstractTransactionService = self.__transaction_translator.get_operation_type(transaction.type)
        service.do(transaction, account)
