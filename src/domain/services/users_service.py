import src.domain.models.users as u
from src.infrastructure.database.repositories import users_repository as ur


class UsersService:
    def __init__(self, **kwargs):
        self.__users_repository: ur.UsersRepository = kwargs.get('users_repository')

    def check_duplicated_document(self, document: str) -> bool:
        existing_user: u.Users = self.__users_repository.find_by_document(document)
        return True if existing_user is not None else False

    def create_user(self, user) -> u.Users:
        return self.__users_repository.save(user)
