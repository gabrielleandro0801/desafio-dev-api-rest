from flask_restful import reqparse

from api.controllers.validators.document_validator import DocumentValidator
from api.controllers.validators.types_validator import StringValidator


class UserValidator:
    def __init__(self, document_validator, string_validator) -> None:
        self.__document_validator: DocumentValidator = document_validator
        self.__string_validator: StringValidator = string_validator

    def validate_post(self) -> dict:
        body = reqparse.RequestParser()

        body.add_argument(
            'name',
            required=True,
            type=self.__string_validator.str_validation(max_length=100),
            help='Param is required and must be a string up to 100 characters'
        )
        body.add_argument(
            'document',
            required=True,
            type=self.__document_validator.validate_document,
            help="Param is required and must be either a valid CPF or CNPJ"
        )
        return body.parse_args()
