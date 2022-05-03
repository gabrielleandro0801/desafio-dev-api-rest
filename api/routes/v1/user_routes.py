from flask_restful import Api

from api.controllers.v1.factories import create_user_application_service, create_user_validator
from api.controllers.v1.user_controller import UserController, UserControllerById


def add_routes(api: Api) -> Api:
    api.add_resource(
        UserController,
        '/v1/users',
        resource_class_kwargs={
            'user_validator': create_user_validator(),
            'application_service': create_user_application_service()
        }
    )

    api.add_resource(
        UserControllerById,
        '/v1/users/<int:user_id>',
        resource_class_kwargs={
            'application_service': create_user_application_service()
        }
    )
    return api
