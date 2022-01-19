import src.domain.models.users as u


class UsersTranslator:
    def __init__(self):
        pass

    def translate_user_from_body(self, body: dict):
        return u.Users(
            name=body.get('name'),
            document=body.get('document')
        )
