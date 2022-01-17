from src.infrastructure.database.repositories import users_repository as ur


class UsersTranslator:
    def __init__(self):
        pass

    def translate_user_from_body(self, body: dict):
        return ur.Users(
            name=body.get('name'),
            document=body.get('document')
        )
