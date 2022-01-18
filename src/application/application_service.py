from src.infrastructure.database.repositories import users_repository as ur
from src.infrastructure.translators.users_translator import UsersTranslator


class ApplicationService:
    def __init__(self, **kwargs):
        self.__users_translator: UsersTranslator = kwargs.get('users_translator')
        self.__users_repository: ur.UsersRepository = kwargs.get('users_repository')

    def register_user(self, body: dict) -> ur.Users or False:
        user: ur.Users = self.__users_translator.translate_user_from_body(body)

        existing_user: ur.Users = self.__users_repository.find_by_document(user.document)
        # if existing_user is None:
        #     return False

        # by_id = self.__users_repository.find_by_user_id(2)
        # self.__users_repository.delete_by_user_id(existing_user)
        return self.__users_repository.save(user)

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
