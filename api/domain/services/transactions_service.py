from abc import ABC, abstractmethod
from typing import List

import api.domain.exceptions.custom_exceptions as ce
from api.domain.models.accounts import Accounts
from api.domain.models.transactions import Transactions

from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository
from api.infrastructure.translators.transactions_translator import TransactionsTranslator


class TransactionService(ABC):

    @abstractmethod
    def do(self, transaction: Transactions, account: Accounts) -> None:
        pass


class DepositService(TransactionService):
    def __init__(self, transactions_repository) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository

    def do(self, transaction: Transactions, _) -> None:
        self.__transactions_repository.save(transaction)


class WithdrawService(TransactionService):
    def __init__(self, transactions_repository, transactions_translator) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository
        self.__transactions_translator: TransactionsTranslator = transactions_translator

    def do(self, transaction: Transactions, account: Accounts) -> None:
        if transaction.value > account.balance:
            raise ce.AccountHasNoEnoughBalance

        withdraws: List[Transactions] = self.__transactions_repository.get_withdraws_of_the_day(account.id)
        total: float = self.__transactions_translator.get_sum_of_withdraws(withdraws)

        if (total + transaction.value) > account.withdraw_daily_limit:
            raise ce.WithdrawSurpassesDailyLimitBalance

        self.__transactions_repository.save(transaction)


class TransactionsService:
    def __init__(self, transactions_repository, transactions_translator) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository
        self.__transactions_translator: TransactionsTranslator = transactions_translator

    def do_transaction(self, body: dict, account: Accounts) -> None:
        transaction: Transactions = self.__transactions_translator.translate_transaction_from_body(body)

        service: TransactionService = self.__transactions_translator.get_operation_type(transaction.type)
        service.do(transaction, account)

    def list_transactions(self, account_id: int, **kwargs) -> dict:
        return self.__transactions_repository.get_transactions_from_period(account_id, **kwargs)
