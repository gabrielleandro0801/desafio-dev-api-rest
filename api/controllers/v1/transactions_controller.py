from http import HTTPStatus

from flask_restful import Resource

import api.domain.custom_exceptions as ce
from api.application.transactions_application_service import TransactionsApplicationService
from api.controllers.validators.transactions_validator import TransactionsValidator


class TransactionsController(Resource):
    def __init__(self, transactions_validator, application_service) -> None:
        self.__transactions_validator: TransactionsValidator = transactions_validator
        self.__application_service: TransactionsApplicationService = application_service

    def post(self):
        body: dict = self.__transactions_validator.validate_post()

        try:
            self.__application_service.do_transaction(body)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountStatusDoesNotAllowToTransact:
            return {
                'message': 'The status of the account does not allow transactions'
            }, HTTPStatus.UNPROCESSABLE_ENTITY
        except ce.AccountHasNoEnoughBalance:
            return {
                'message': 'This account does not have enough balance'
            }, HTTPStatus.UNPROCESSABLE_ENTITY
        except ce.WithdrawSurpassesDailyLimitBalance:
            return {
                'message': 'This withdraw will surpass the daily limit'
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return {
            'message': 'Transaction successfully performed'
        }, HTTPStatus.CREATED

    def get(self):
        arguments: dict = self.__transactions_validator.validate_get()

        try:
            response: dict = self.__application_service.list_transactions(**arguments)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountStatusDoesNotAllowToListTransactions:
            return {
                'message': 'The status of the account does not allow to consult the transactions'
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return response, HTTPStatus.OK
