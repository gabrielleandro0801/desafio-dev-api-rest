from flask_restful import reqparse
from src.controllers.validators.document_validator import DocumentValidator


class UsersValidator:
    def __init__(self, documents_validator):
        self.__document_validator: DocumentValidator = documents_validator

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
            type=self.__document_validator.validate_document,
            help="Param is required and must be either a valid CPF or CNPJ"
        )
        return body.parse_args()
