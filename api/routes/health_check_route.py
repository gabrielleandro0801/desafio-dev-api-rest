from flask_restful import Api

from api.controllers.health_check_controller import HealthCheckController


def add_routes(api: Api) -> Api:
    api.add_resource(
        HealthCheckController,
        '/',
        resource_class_kwargs={}
    )

    return api
