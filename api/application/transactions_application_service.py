import api.domain.custom_exceptions as ce

from api.domain.models.accounts import Accounts

from api.domain.services.accounts_service import AccountsService
from api.domain.services.transactions_service import TransactionsService

from api.domain.validators.account_status_validator import AccountStatusValidator
from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository


class TransactionsApplicationService:
    def __init__(self, **kwargs):
        self.__account_status_validator: AccountStatusValidator = kwargs.get('account_status_validator')
        self.__accounts_service: AccountsService = kwargs.get('accounts_service')
        self.__accounts_repository: AccountsRepository = kwargs.get('accounts_repository')
        self.__transactions_service: TransactionsService = kwargs.get('transactions_service')
        self.__transactions_repository: TransactionsRepository = kwargs.get('transactions_repository')

    def do_transaction(self, body: dict) -> None:
        account: Accounts = self.__accounts_repository.find_by_account_id(body.get('accountId'))
        if account is None:
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_do_transaction(account.status)
        if not is_valid:
            raise ce.AccountStatusDoesNotAllowToTransact

        self.__transactions_service.do_transaction(body, account)
        self.__accounts_service.update_balance(account, body.get('amount'), body.get('operationType'))

    def list_transactions(self, **kwargs) -> dict:
        account: Accounts = self.__accounts_repository.find_by_account_id(kwargs.get('accountId'))
        if account is None:
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_list_transactions(account.status)
        if not is_valid:
            raise ce.AccountStatusDoesNotAllowToListTransactions

        return self.__transactions_repository.get_transactions_from_period(**kwargs)
