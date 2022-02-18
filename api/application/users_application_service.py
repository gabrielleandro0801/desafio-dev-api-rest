import api.domain.custom_exceptions as ce

from api.domain.models.users import Users
from api.domain.services.accounts_service import AccountsService
from api.domain.services.users_service import UsersService
from api.infrastructure.database.repositories.users_repository import UsersRepository


class UsersApplicationService:
    def __init__(self, **kwargs):
        self.__users_service: UsersService = kwargs.get('users_service')
        self.__users_repository: UsersRepository = kwargs.get('users_repository')
        self.__accounts_service: AccountsService = kwargs.get('accounts_service')

    def register_user(self, body: dict) -> Users:
        doc_already_exists: bool = self.__users_service.check_duplicated_document(body.get('document'))
        if doc_already_exists:
            raise ce.DocumentAlreadyExists

        return self.__users_service.create_user(body)

    def remove_user(self, user_id: int) -> None:
        user: Users = self.__users_repository.find_by_user_id(user_id)
        if user is None:
            raise ce.UserNotFound

        user_has_account: bool = self.__accounts_service.retrieve_existing_account_by_user_id(user.id)
        if user_has_account:
            raise ce.UserHasAccount

        self.__users_repository.delete(user)
