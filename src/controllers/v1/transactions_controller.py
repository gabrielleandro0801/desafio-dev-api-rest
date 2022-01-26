from http import HTTPStatus

from flask_restful import Resource

import src.domain.exceptions.custom_exceptions as ce
from src.application.application_service import ApplicationService
from src.controllers.validators.transactions_validator import TransactionsValidator


class TransactionsController(Resource):
    def __init__(self, transactions_validator, application_service) -> None:
        self.__transactions_validator: TransactionsValidator = transactions_validator
        self.__application_service: ApplicationService = application_service

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
            }, HTTPStatus.BAD_REQUEST
        except ce.AccountHasNoEnoughBalance:
            return {
                'message': 'This account does not have enough balance'
            }, HTTPStatus.BAD_REQUEST
        except ce.WithdrawSurpassesDailyLimitBalance:
            return {
                'message': 'This withdraw will surpass the daily limit'
            }, HTTPStatus.BAD_REQUEST

        return {
            'message': 'Transaction successfully performed'
        }, HTTPStatus.CREATED


class TransactionsControllerByAccountId(Resource):
    def __init__(self, transactions_validator, application_service) -> None:
        self.__transactions_validator: TransactionsValidator = transactions_validator
        self.__application_service: ApplicationService = application_service

    def get(self, account_id: int):
        arguments: dict = self.__transactions_validator.validate_get()

        try:
            response: dict = self.__application_service.get_transactions(account_id, **arguments)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountStatusDoesNotAllowToListTransactions:
            return {
                'message': 'The status of the account does not allow to consult the transactions'
            }, HTTPStatus.BAD_REQUEST

        return response, HTTPStatus.OK
