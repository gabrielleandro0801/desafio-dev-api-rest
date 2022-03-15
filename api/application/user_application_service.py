import api.domain.custom_exceptions as ce

from api.domain.models.user import User
from api.domain.services.account_service import AccountService
from api.domain.services.user_service import UserService
from api.infrastructure.database.repositories.users_repository import UsersRepository
from api.infrastructure.log import logger


class UserApplicationService:
    def __init__(self, **kwargs):
        self.__user_service: UserService = kwargs.get('users_service')
        self.__users_repository: UsersRepository = kwargs.get('users_repository')
        self.__account_service: AccountService = kwargs.get('accounts_service')

    def register_user(self, body: dict) -> User:
        logger.info({"message": "Creating user", "body": body})
        doc_already_exists: bool = self.__user_service.check_duplicated_document(body.get('document'))

        if doc_already_exists:
            logger.warning({"message": "This document already exists"})
            raise ce.DocumentAlreadyExists

        return self.__user_service.create_user(body)

    def remove_user(self, user_id: int) -> None:
        logger.info({"message": "Deleting user", "id": user_id})
        user: User = self.__users_repository.find_by_user_id(user_id)

        if user is None:
            logger.warning({"message": "No users found", "id": user_id})
            raise ce.UserNotFound

        user_has_account: bool = self.__account_service.retrieve_existing_account_by_user_id(user.id)
        if user_has_account:
            logger.warning({"message": "This user has an active account"})
            raise ce.UserHasAccount

        self.__users_repository.delete(user)
