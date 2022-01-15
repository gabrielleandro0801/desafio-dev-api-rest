from flask_restful import Api

import src.application.application_service as ap
import src.controllers.v1.users.users_controller as u
import src.controllers.validators.users_validator as uv
from src.infrastructure.database.repositories.users import Users


def add_routes(api: Api) -> Api:
    api.add_resource(
        u.Users,
        '/v1/users',
        resource_class_kwargs={
            'users_validator': uv.UsersValidator(),
            'application_service': ap.ApplicationService(users_repository=Users)
        }
    )
    return api
