import src.domain.exceptions.custom_exceptions as ce
import src.domain.models.accounts as a
import src.domain.models.users as u
from src.domain.services.accounts_service import AccountsService
from src.domain.services.users_service import UsersService
from src.infrastructure.translators.users_translator import UsersTranslator


class ApplicationService:
    def __init__(self, **kwargs):
        self.__users_translator: UsersTranslator = kwargs.get('users_translator')
        self.__users_service: UsersService = kwargs.get('users_service')
        self.__accounts_service: AccountsService = kwargs.get('accounts_service')

    def register_user(self, body: dict) -> u.Users:
        user: u.Users = self.__users_translator.translate_user_from_body(body)

        doc_already_exists: bool = self.__users_service.check_duplicated_document(user.document)
        if doc_already_exists:
            raise ce.DocumentAlreadyExists

        return self.__users_service.create_user(user)

    def remove_user(self, user_id: int) -> None:
        user: u.Users = self.__users_service.get_user_by_id(user_id)
        if user is None:
            raise ce.UserNotFound

        self.__users_service.delete_user(user)

    def register_account(self, body: dict) -> a.Accounts:
        user: u.Users = self.__users_service.get_user_by_id(body.get('userId'))
        if user is None:
            raise ce.UserNotFound

        account_already_exists: bool = self.__accounts_service.check_duplicated_account(user.id)
        if account_already_exists:
            raise ce.AccountAlreadyExists

        return self.__accounts_service.create_account(user)

    def retrieve_account(self):
        pass

    def lock_account(self):
        pass

    def unlock_account(self):
        pass

    def close_account(self):
        pass

    def do_deposit(self):
        pass

    def do_withdraw(self):
        pass
