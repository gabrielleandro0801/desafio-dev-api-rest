from flask_restful import reqparse

from src.controllers.validators.types_validator import IntValidator


class AccountsValidator:
    def __init__(self, int_validator):
        self.__int_validator: IntValidator = int_validator

    def validate_post(self) -> dict:
        body = reqparse.RequestParser()

        body.add_argument(
            'userId',
            required=True,
            type=self.__int_validator.validate,
            help='Param is required and must be a valid number'
        )
        return body.parse_args()
