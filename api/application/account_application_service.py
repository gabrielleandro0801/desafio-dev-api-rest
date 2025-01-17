import api.domain.custom_exceptions as ce

from api.domain.models.account import Account
from api.domain.models.user import User
from api.domain.services.account_service import AccountService
from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
from api.infrastructure.database.repositories.users_repository import UsersRepository
from api.infrastructure.log import logger


class AccountApplicationService:
    def __init__(self, **kwargs):
        self.__users_repository: UsersRepository = kwargs.get('users_repository')
        self.__accounts_repository: AccountsRepository = kwargs.get('accounts_repository')
        self.__account_service: AccountService = kwargs.get('account_service')

    def register_account(self, body: dict) -> Account:
        logger.info({"message": "Creating account", "body": body})
        user: User = self.__users_repository.find_by_user_id(body.get('userId'))

        if user is None:
            logger.warning({"message": "No users found", "id": body.get('userId')})
            raise ce.UserNotFound

        logger.info({"message": "Finding account by user id", "id": body.get('userId')})
        account_already_exists: bool = self.__account_service.retrieve_existing_account_by_user_id(user.id)

        if account_already_exists:
            logger.warning({"message": "There is already an account for this user", "id": body.get('userId')})
            raise ce.AccountAlreadyExists

        return self.__account_service.create_account(user)

    def retrieve_account(self, account_id: int) -> Account:
        logger.info({"message": "Finding account", "id": account_id})
        account: Account = self.__accounts_repository.find_by_account_id(account_id)

        if account is None:
            logger.warning({"message": "No accounts found", "id": account_id})
            raise ce.AccountNotFound

        return account

    def close_account(self, account_id: int) -> None:
        logger.info({"message": "Closing account", "id": account_id})
        account: Account = self.__accounts_repository.find_by_account_id(account_id)

        if account is None:
            logger.warning({"message": "No accounts found", "id": account_id})
            raise ce.AccountNotFound

        is_able_to_close: bool = account.is_able_to_close()
        if not is_able_to_close:
            logger.warning({"message": "This account is not able to close", "id": account_id})
            raise ce.AccountStatusDoesNotAllowToClose

        self.__accounts_repository.close_account(account)

    def lock_account(self, account_id: int) -> None:
        logger.info({"message": "Locking account", "id": account_id})
        account: Account = self.__accounts_repository.find_by_account_id(account_id)

        if account is None:
            logger.warning({"message": "No accounts found", "id": account_id})
            raise ce.AccountNotFound

        is_able_to_lock: bool = account.is_able_to_lock()
        if not is_able_to_lock:
            logger.warning({"message": "This account is not able to lock", "id": account_id})
            raise ce.AccountStatusDoesNotAllowToLock

        self.__account_service.lock_account(account)

    def unlock_account(self, account_id: int) -> None:
        logger.info({"message": "Unlocking account", "id": account_id})
        account: Account = self.__accounts_repository.find_by_account_id(account_id)

        if account is None:
            logger.warning({"message": "No accounts found", "id": account_id})
            raise ce.AccountNotFound

        is_able_to_unlock: bool = account.is_able_to_unlock()
        if not is_able_to_unlock:
            logger.warning({"message": "This account is not able to unlock", "id": account_id})
            raise ce.AccountStatusDoesNotAllowToUnLock

        self.__account_service.unlock_account(account)
