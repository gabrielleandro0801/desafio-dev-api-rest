from flask_restful import Api

from src.controllers.v1.factories import create_application_service, create_user_validator
from src.controllers.v1.users_controller import UsersController, UsersControllerById


def add_routes(api: Api) -> Api:
    api.add_resource(
        UsersController,
        '/v1/users',
        resource_class_kwargs={
            'users_validator': create_user_validator(),
            'application_service': create_application_service()
        }
    )

    api.add_resource(
        UsersControllerById,
        '/v1/users/<user_id>',
        resource_class_kwargs={
            'application_service': create_application_service()
        }
    )
    return api
