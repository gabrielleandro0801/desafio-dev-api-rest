from flask_restful import reqparse

from src.controllers.validators.float_validator import FloatValidator
from src.domain.models.transactions import TransactionTypes


class TransactionsValidator:
    def __init__(self, transaction_types, float_validator) -> None:
        self.__transaction_types: TransactionTypes = transaction_types
        self.__float_validator: FloatValidator = float_validator

    def validate_post(self) -> dict:
        body = reqparse.RequestParser()

        body.add_argument(
            'accountId',
            required=True,
            type=int,
            help='Param is required and must be a valid number'
        )
        body.add_argument(
            'amount',
            required=True,
            type=self.__float_validator.validate,
            help='Param is required and must be a valid number'
        )
        body.add_argument(
            'operationType',
            required=True,
            choices=(
                self.__transaction_types.DEPOSIT,
                self.__transaction_types.WITHDRAW
            ),
            help='Param is required and must be a valid operation - DEPOSIT or WITHDRAW'
        )

        return body.parse_args()
