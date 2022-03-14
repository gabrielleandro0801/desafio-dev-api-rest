from api.domain.models.user import User
from api.infrastructure.database.repositories.users_repository import UsersRepository
from api.infrastructure.translators.user_translator import UserTranslator


class UserService:
    def __init__(self, **kwargs):
        self.__user_translator: UserTranslator = kwargs.get('user_translator')
        self.__users_repository: UsersRepository = kwargs.get('users_repository')

    def check_duplicated_document(self, document: str) -> bool:
        existing_user: User = self.__users_repository.find_by_document(document)
        return True if existing_user is not None else False

    def create_user(self, body: dict) -> User:
        user: User = self.__user_translator.translate_user_from_body(body)
        return self.__users_repository.save(user)
