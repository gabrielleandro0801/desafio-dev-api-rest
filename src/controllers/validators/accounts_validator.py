from flask_restful import reqparse


class AccountsValidator:

    @classmethod
    def validate_post(cls) -> dict:
        body = reqparse.RequestParser()

        body.add_argument(
            'userId',
            required=True,
            type=int,
            help='Param is required and must be a valid number'
        )
        return body.parse_args()
