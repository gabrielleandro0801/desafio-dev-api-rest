import src.domain.models.users as u
from src.domain.exceptions.custom_exceptions import DocumentAlreadyExists
from src.domain.services.users_service import UsersService
from src.infrastructure.translators.users_translator import UsersTranslator


class ApplicationService:
    def __init__(self, **kwargs):
        self.__users_translator: UsersTranslator = kwargs.get('users_translator')
        self.__users_service: UsersService = kwargs.get('users_service')

    def register_user(self, body: dict) -> u.Users:
        user: u.Users = self.__users_translator.translate_user_from_body(body)

        doc_already_exists: bool = self.__users_service.check_duplicated_document(user.document)
        if doc_already_exists:
            raise DocumentAlreadyExists

        return self.__users_service.create_user(user)

    def remove_user(self):
        pass

    def register_account(self):
        pass

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
