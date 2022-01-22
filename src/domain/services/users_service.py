import src.domain.models.users as u
from src.infrastructure.database.repositories import users_repository as ur
from src.infrastructure.translators.users_translator import UsersTranslator


class UsersService:
    def __init__(self, **kwargs):
        self.__users_translator: UsersTranslator = kwargs.get('users_translator')
        self.__users_repository: ur.UsersRepository = kwargs.get('users_repository')

    def check_duplicated_document(self, document: str) -> bool:
        existing_user: u.Users = self.__users_repository.find_by_document(document)
        return True if existing_user is not None else False

    def create_user(self, body: dict) -> u.Users:
        user: u.Users = self.__users_translator.translate_user_from_body(body)
        return self.__users_repository.save(user)

    def get_user_by_id(self, user_id: int) -> u.Users or None:
        return self.__users_repository.find_by_user_id(user_id)

    def delete_user(self, user: u.Users) -> None:
        self.__users_repository.delete(user)
