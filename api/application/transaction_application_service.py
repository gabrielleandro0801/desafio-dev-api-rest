import api.domain.custom_exceptions as ce

from api.domain.models.account import Account

from api.domain.services.account_service import AccountService
from api.domain.services.transaction_service import TransactionService

from api.domain.validators.account_status_validator import AccountStatusValidator
from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository
from api.infrastructure.log import logger


class TransactionApplicationService:
    def __init__(self, **kwargs):
        self.__account_status_validator: AccountStatusValidator = kwargs.get('account_status_validator')
        self.__account_service: AccountService = kwargs.get('accounts_service')
        self.__accounts_repository: AccountsRepository = kwargs.get('accounts_repository')
        self.__transaction_service: TransactionService = kwargs.get('transactions_service')
        self.__transactions_repository: TransactionsRepository = kwargs.get('transactions_repository')

    def do_transaction(self, body: dict) -> None:
        logger.info({"message": "Performing transaction", "body": body})
        account: Account = self.__accounts_repository.find_by_account_id(body.get('accountId'))

        if account is None:
            logger.warning({"message": "No accounts found", "id": body.get('accountId')})
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_do_transaction(account.status)
        if not is_valid:
            logger.warning({"message": "This account is not able to do transactions", "id": body.get('accountId')})
            raise ce.AccountStatusDoesNotAllowToTransact

        self.__transaction_service.do_transaction(body, account)
        self.__account_service.update_balance(account, body.get('amount'), body.get('operationType'))

    def list_transactions(self, **kwargs) -> dict:
        logger.info({"message": "Listing transactions", "id": kwargs.get('accountId')})
        account: Account = self.__accounts_repository.find_by_account_id(kwargs.get('accountId'))

        if account is None:
            logger.warning({"message": "No accounts found", "id": kwargs.get('accountId')})
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_list_transactions(account.status)
        if not is_valid:
            logger.warning({"message": "This account is not able to list transactions", "id": kwargs.get('accountId')})
            raise ce.AccountStatusDoesNotAllowToListTransactions

        return self.__transactions_repository.get_transactions_from_period(**kwargs)
