import api.domain.custom_exceptions as ce

from api.domain.models.account import Account
from api.domain.models.user import User
from api.domain.services.account_service import AccountService
from api.domain.validators.account_status_validator import AccountStatusValidator
from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
from api.infrastructure.database.repositories.users_repository import UsersRepository


class AccountApplicationService:
    def __init__(self, **kwargs):
        self.__users_repository: UsersRepository = kwargs.get('users_repository')
        self.__accounts_repository: AccountsRepository = kwargs.get('accounts_repository')
        self.__account_service: AccountService = kwargs.get('account_service')
        self.__account_status_validator: AccountStatusValidator = kwargs.get('account_status_validator')

    def register_account(self, body: dict) -> Account:
        user: User = self.__users_repository.find_by_user_id(body.get('userId'))
        if user is None:
            raise ce.UserNotFound

        account_already_exists: bool = self.__account_service.retrieve_existing_account_by_user_id(user.id)
        if account_already_exists:
            raise ce.AccountAlreadyExists

        return self.__account_service.create_account(user)

    def retrieve_account(self, account_id: int) -> Account:
        account: Account = self.__accounts_repository.find_by_account_id(account_id)
        if account is None:
            raise ce.AccountNotFound

        return account

    def close_account(self, account_id: int) -> None:
        account: Account = self.__accounts_repository.find_by_account_id(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_close: bool = self.__account_status_validator.validate_status_to_close_account(account.status)
        if not is_able_to_close:
            raise ce.AccountStatusDoesNotAllowToClose

        self.__accounts_repository.close_account(account)

    def lock_account(self, account_id: int) -> None:
        account: Account = self.__accounts_repository.find_by_account_id(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_lock: bool = self.__account_status_validator.validate_status_to_lock_account(account.status)
        if not is_able_to_lock:
            raise ce.AccountStatusDoesNotAllowToLock

        self.__account_service.lock_account(account)

    def unlock_account(self, account_id: int) -> None:
        account: Account = self.__accounts_repository.find_by_account_id(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_unlock: bool = self.__account_status_validator.validate_status_to_unlock_account(account.status)
        if not is_able_to_unlock:
            raise ce.AccountStatusDoesNotAllowToUnLock

        self.__account_service.unlock_account(account)
