from api.domain.models.users import Users
from api.infrastructure.database.repositories.users_repository import UsersRepository
from api.infrastructure.translators.users_translator import UsersTranslator


class UsersService:
    def __init__(self, **kwargs):
        self.__users_translator: UsersTranslator = kwargs.get('users_translator')
        self.__users_repository: UsersRepository = kwargs.get('users_repository')

    def check_duplicated_document(self, document: str) -> bool:
        existing_user: Users = self.__users_repository.find_by_document(document)
        return True if existing_user is not None else False

    def create_user(self, body: dict) -> Users:
        user: Users = self.__users_translator.translate_user_from_body(body)
        return self.__users_repository.save(user)
