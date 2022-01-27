import api.domain.exceptions.custom_exceptions as ce

from api.domain.models.accounts import Accounts
from api.domain.models.users import Users

from api.domain.services.accounts_service import AccountsService
from api.domain.services.transactions_service import TransactionsService
from api.domain.services.users_service import UsersService

from api.domain.validators.account_status_validator import AccountStatusValidator


class ApplicationService:
    def __init__(self, **kwargs) -> None:
        self.__users_service: UsersService = kwargs.get('users_service')
        self.__accounts_service: AccountsService = kwargs.get('accounts_service')
        self.__transactions_service: TransactionsService = kwargs.get('transactions_service')
        self.__account_status_validator: AccountStatusValidator = kwargs.get('account_status_validator')

    def register_user(self, body: dict) -> Users:
        doc_already_exists: bool = self.__users_service.check_duplicated_document(body.get('document'))
        if doc_already_exists:
            raise ce.DocumentAlreadyExists

        return self.__users_service.create_user(body)

    def remove_user(self, user_id: int) -> None:
        user: Users = self.__users_service.get_user_by_id(user_id)
        if user is None:
            raise ce.UserNotFound

        user_has_account: bool = self.__accounts_service.get_existing_account_by_user_id(user.id)
        if user_has_account:
            raise ce.UserHasAccount

        self.__users_service.delete_user(user)

    def register_account(self, body: dict) -> Accounts:
        user: Users = self.__users_service.get_user_by_id(body.get('userId'))
        if user is None:
            raise ce.UserNotFound

        account_already_exists: bool = self.__accounts_service.get_existing_account_by_user_id(user.id)
        if account_already_exists:
            raise ce.AccountAlreadyExists

        return self.__accounts_service.create_account(user)

    def retrieve_account(self, account_id: int) -> Accounts:
        account: Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        return account

    def close_account(self, account_id: int) -> None:
        account: Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_close: bool = self.__account_status_validator.validate_status_to_close_account(account.status)
        if not is_able_to_close:
            raise ce.AccountStatusDoesNotAllowToClose

        self.__accounts_service.close_account(account)

    def lock_account(self, account_id: int) -> None:
        account: Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_lock: bool = self.__account_status_validator.validate_status_to_lock_account(account.status)
        if not is_able_to_lock:
            raise ce.AccountStatusDoesNotAllowToLock

        self.__accounts_service.lock_account(account)

    def unlock_account(self, account_id: int) -> None:
        account: Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_unlock: bool = self.__account_status_validator.validate_status_to_unlock_account(account.status)
        if not is_able_to_unlock:
            raise ce.AccountStatusDoesNotAllowToUnLock

        self.__accounts_service.unlock_account(account)

    def do_transaction(self, body: dict) -> None:
        account: Accounts = self.__accounts_service.get_account(body.get('accountId'))
        if account is None:
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_do_transaction(account.status)
        if not is_valid:
            raise ce.AccountStatusDoesNotAllowToTransact

        self.__transactions_service.do_transaction(body, account)
        self.__accounts_service.update_balance(account, body.get('amount'), body.get('operationType'))

    def get_transactions(self, account_id: int, **kwargs) -> dict:
        account: Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_list_transactions(account.status)
        if not is_valid:
            raise ce.AccountStatusDoesNotAllowToListTransactions

        return self.__transactions_service.list_transactions(account_id, **kwargs)
