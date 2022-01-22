from abc import ABC, abstractmethod
from typing import List

import src.domain.exceptions.custom_exceptions as ce
import src.domain.models.accounts as a
import src.domain.models.transactions as t

from src.infrastructure.database.repositories.transactions_repository import TransactionsRepository
from src.infrastructure.translators.transactions_translator import TransactionsTranslator


class TransactionsService(ABC):

    @abstractmethod
    def do(self, transaction: t.Transactions, account: a.Accounts) -> None:
        pass


class DepositService(TransactionsService):
    def __init__(self, transactions_repository) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository

    def do(self, transaction: t.Transactions, _) -> None:
        self.__transactions_repository.save(transaction)


class WithdrawService(TransactionsService):
    def __init__(self, transactions_repository, transactions_translator) -> None:
        self.__transactions_repository: TransactionsRepository = transactions_repository
        self.__transactions_translator: TransactionsTranslator = transactions_translator

    def do(self, transaction: t.Transactions, account: a.Accounts) -> None:
        if transaction.value > account.balance:
            raise ce.AccountHasNoEnoughBalance

        withdraws_of_the_day: List[t.Transactions] = self.__transactions_repository.get_account_withdraws_of_the_day(account.id)
        total: float = self.__transactions_translator.get_sum_of_withdraws(withdraws_of_the_day)

        if total + transaction.value > account.withdraw_daily_limit:
            raise ce.WithdrawSurpassesDailyLimitBalance

        self.__transactions_repository.save(transaction)
