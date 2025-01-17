from http import HTTPStatus
from flask_restful import Resource

import api.domain.custom_exceptions as ce
from api.application.account_application_service import AccountApplicationService
from api.controllers.validators.account_validator import AccountValidator
from api.domain.models.account import Account


class AccountController(Resource):
    def __init__(self, account_validator, application_service) -> None:
        self.__account_validator: AccountValidator = account_validator
        self.__application_service: AccountApplicationService = application_service

    def post(self):
        body: dict = self.__account_validator.validate_post()

        try:
            account: Account = self.__application_service.register_account(body)
        except ce.UserNotFound:
            return {
                'message': 'User not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountAlreadyExists:
            return {
                'message': 'This account already exists'
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return {
           'accountId': account.id,
           'accountNumber': account.number,
           'bankBranch': account.bank_branch,
           'withdrawDailyLimit': account.withdraw_daily_limit
        }, HTTPStatus.CREATED


class AccountControllerById(Resource):
    def __init__(self, application_service) -> None:
        self.__application_service: AccountApplicationService = application_service

    def get(self, account_id: int):
        try:
            account: Account = self.__application_service.retrieve_account(account_id)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND

        return {
            'status': account.status,
            'accountNumber': account.number,
            'bankBranch': account.bank_branch,
            'transferDailyLimit': account.withdraw_daily_limit,
            'balance': account.balance,
            'userId': account.user_id
        }, HTTPStatus.OK

    def delete(self, account_id: int):
        try:
            self.__application_service.close_account(account_id)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountStatusDoesNotAllowToClose:
            return {
                'message': 'The account must be active in order to be closed'
            }, HTTPStatus.CONFLICT

        return '', HTTPStatus.NO_CONTENT


class AccountLockControllerById(Resource):
    def __init__(self, application_service) -> None:
        self.__application_service: AccountApplicationService = application_service

    def post(self, account_id: int):
        try:
            self.__application_service.lock_account(account_id)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountStatusDoesNotAllowToLock:
            return {
                'message': 'The account must be active in order to be locked'
            }, HTTPStatus.CONFLICT

        return '', HTTPStatus.NO_CONTENT

    def delete(self, account_id: int):
        try:
            self.__application_service.unlock_account(account_id)
        except ce.AccountNotFound:
            return {
                'message': 'Account not found'
            }, HTTPStatus.NOT_FOUND
        except ce.AccountStatusDoesNotAllowToUnLock:
            return {
                'message': 'The account must be locked in order to be unlocked'
            }, HTTPStatus.CONFLICT

        return '', HTTPStatus.NO_CONTENT
