from src.infrastructure.database.repositories import users_repository as ur
from src.infrastructure.database.repositories.users_repository import UsersRepository
from src.infrastructure.translators.users_translator import UsersTranslator


class ApplicationService:
    def __init__(self, **kwargs):
        self.__users_translator: UsersTranslator = kwargs.get('users_translator')
        self.__users_repository: UsersRepository = kwargs.get('users_repository')

    def register_user(self, body: dict):
        user: ur.Users = self.__users_translator.translate_user_from_body(body)

        existing_user = self.__users_repository.find_by_document(user.document)
        if existing_user is not None:
            return False

        # self.__users_repository.save()


