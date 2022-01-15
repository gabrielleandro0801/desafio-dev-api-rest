from flask_restful import reqparse, inputs


class UsersValidator:
    def __init__(self):
        pass

    def validate_post(self) -> dict:
        body = reqparse.RequestParser()

        body.add_argument(
            'name',
            required=True,
            type=str,
            help='Param is required and must be a string'
        )
        body.add_argument(
            'document',
            required=True,
            type=inputs.regex('^[0-9]{11}$'),
            help="Param is required and must be only numbers and its length must be 11 or 14"
        )
        return body.parse_args()
