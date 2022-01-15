import src.domain.models.users as u
from src.infrastructure.database.repositories.users import Users


class ApplicationService:
    def __init__(self, **kwargs):
        self.__users_repository: Users = kwargs.get('users_repository')

    def register_user(self, body):
        existing_user: None or u.Users = self.__users_repository.find(document=body.get('document'))
        if existing_user is not None:
            return False


