from api.domain.models.user import User


class UserTranslator:

    @classmethod
    def translate_user_from_body(cls, body: dict):
        return User(
            name=body.get('name'),
            document=body.get('document')
        )
