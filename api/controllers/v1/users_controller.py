from http import HTTPStatus
from flask_restful import Resource

import api.domain.custom_exceptions as ce
from api.application.users_application_service import UsersApplicationService
from api.controllers.validators.users_validator import UsersValidator
from api.domain.models.users import Users


class UsersController(Resource):
    def __init__(self, users_validator, application_service) -> None:
        self.__users_validator: UsersValidator = users_validator
        self.__application_service: UsersApplicationService = application_service

    def post(self):
        body: dict = self.__users_validator.validate_post()

        try:
            response: Users = self.__application_service.register_user(body)
        except ce.DocumentAlreadyExists:
            return {
                'message': 'There is already a user using this document'
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return {
            'message': 'User successfully created',
            'id': response.id
        }, HTTPStatus.CREATED


class UsersControllerById(Resource):
    def __init__(self, application_service) -> None:
        self.__application_service: UsersApplicationService = application_service

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
