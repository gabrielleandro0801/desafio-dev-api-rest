import src.domain.models.users as u


class UsersTranslator:
    def __init__(self):
        pass

    @classmethod
    def translate_user_from_body(cls, body: dict):
        return u.Users(
            name=body.get('name'),
            document=body.get('document')
        )
