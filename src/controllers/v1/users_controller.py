from http import HTTPStatus
from flask_restful import Resource

import src.domain.exceptions.custom_exceptions as ce
import src.domain.models.users as u

from src.application.application_service import ApplicationService
from src.controllers.validators.users_validator import UsersValidator


class UsersController(Resource):
    def __init__(self, users_validator, application_service) -> None:
        self.__users_validator: UsersValidator = users_validator
        self.__application_service: ApplicationService = application_service

    def post(self):
        body: dict = self.__users_validator.validate_post()

        try:
            response: u.Users = self.__application_service.register_user(body)
        except ce.DocumentAlreadyExists:
            return {
                'message': 'There is already a user using this document'
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return {
            'message': 'User successfully created',
            'userId': response.id
        }, HTTPStatus.CREATED


class UsersControllerById(Resource):
    def __init__(self, application_service) -> None:
        self.__application_service: ApplicationService = application_service

    def delete(self, user_id: int):
        try:
            self.__application_service.remove_user(user_id)
        except ce.UserNotFound:
            return {
                'message': 'User not found'
            }, HTTPStatus.NOT_FOUND

        return '', HTTPStatus.NO_CONTENT
