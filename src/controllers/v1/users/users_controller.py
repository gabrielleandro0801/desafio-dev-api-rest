from http import HTTPStatus

from flask_restful import Resource

from src.application.application_service import ApplicationService
from src.controllers.validators.users_validator import UsersValidator
from src.infrastructure.database.repositories import users_repository as ur


class UsersController(Resource):
    def __init__(self, users_validator, application_service) -> None:
        self.__users_validator: UsersValidator = users_validator
        self.__application_service: ApplicationService = application_service

    def post(self):
        body: dict = self.__users_validator.validate_post()
        response: ur.Users = self.__application_service.register_user(body)
        return {
            'message': 'User successfully created',
            'id': response.id
        }, HTTPStatus.CREATED

