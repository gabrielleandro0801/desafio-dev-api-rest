from http import HTTPStatus
from flask_restful import Resource

import api.domain.custom_exceptions as ce
from api.application.user_application_service import UserApplicationService
from api.controllers.validators.user_validator import UserValidator
from api.domain.models.user import User


class UserController(Resource):
    def __init__(self, user_validator, application_service) -> None:
        self.__user_validator: UserValidator = user_validator
        self.__application_service: UserApplicationService = application_service

    def post(self):
        body: dict = self.__user_validator.validate_post()

        try:
            response: User = self.__application_service.register_user(body)
        except ce.DocumentAlreadyExists:
            return {
                'message': 'There is already a user using this document'
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return {
            'message': 'User successfully created',
            'id': response.id
        }, HTTPStatus.CREATED


class UserControllerById(Resource):
    def __init__(self, application_service) -> None:
        self.__application_service: UserApplicationService = application_service

    def delete(self, user_id: int):
        try:
            self.__application_service.remove_user(user_id)
        except ce.UserNotFound:
            return {
                'message': 'User not found'
            }, HTTPStatus.NOT_FOUND
        except ce.UserHasAccount:
            return {
                'message': "This user can't be removed because he's got an account"
            }, HTTPStatus.BAD_REQUEST

        return '', HTTPStatus.NO_CONTENT
