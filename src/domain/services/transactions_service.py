from abc import ABC, abstractmethod

import src.domain.models.transactions as t
from src.domain.services.accounts_service import AccountsService
from src.domain.validators.account_status_validator import AccountStatusValidator
from src.infrastructure.database.repositories.transactions_repository import TransactionsRepository
from src.infrastructure.translators.transactions_translator import TransactionsTranslator


class TransactionsService(ABC):

    @abstractmethod
    def do(self, body: dict) -> None:
        pass


class DepositService(TransactionsService):
    def __init__(self, **kwargs) -> None:
        self.__transactions_repository: TransactionsRepository = kwargs.get('transactions_repository')

    def do(self, transaction: t.Transactions) -> None:
        self.__transactions_repository.save(transaction)


class WithdrawService(TransactionsService):
    def __init__(self):
        pass

    def do(self, body: dict) -> None:
        pass
