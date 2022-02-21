from flask_restful import reqparse

from api.controllers.validators.types_validator import FloatValidator, DateValidator, IntValidator
from api.domain.models.transactions import TransactionTypes


class TransactionsValidator:
    def __init__(self, transaction_types, float_validator, int_validator, date_validator) -> None:
        self.__transaction_types: TransactionTypes = transaction_types
        self.__float_validator: FloatValidator = float_validator
        self.__int_validator: IntValidator = int_validator
        self.__date_validator: DateValidator = date_validator

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

    def validate_get(self) -> dict:
        body = reqparse.RequestParser()

        body.add_argument(
            'accountId',
            required=True,
            type=self.__int_validator.validate,
            location='args',
            help='Param is required and must be a valid and positive number'
        )

        body.add_argument(
            'from',
            required=False,
            type=self.__date_validator.validate,
            location='args',
            help='Param is optional and must be a valid date in ISO-8061 format (YYYY-MM-DDT00:00:00.000Z)'
        )

        body.add_argument(
            'to',
            required=False,
            type=self.__date_validator.validate,
            location='args',
            help='Param is optional and must be a valid date in ISO-8061 format (YYYY-MM-DDT00:00:00.000Z)',
        )

        body.add_argument(
            'page',
            required=False,
            type=self.__int_validator.validate,
            default=0,
            location='args',
            help='Param is optional and must be a valid and positive number',
        )

        body.add_argument(
            'limit',
            required=False,
            type=self.__int_validator.validate,
            default=50,
            location='args',
            help='Param is optional and must be a valid and positive number'
        )
        return body.parse_args()
