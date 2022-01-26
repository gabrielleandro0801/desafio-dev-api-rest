from src.domain.models.users import Users


class UsersTranslator:

    @classmethod
    def translate_user_from_body(cls, body: dict):
        return Users(
            name=body.get('name'),
            document=body.get('document')
        )
