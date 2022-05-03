from flask_restful import Api

from api.controllers.v1.account_controller import AccountController, AccountControllerById, \
    AccountLockControllerById
from api.controllers.v1.factories import create_account_validator, create_account_application_service


def add_routes(api: Api) -> Api:
    api.add_resource(
        AccountController,
        '/v1/accounts',
        resource_class_kwargs={
            'account_validator': create_account_validator(),
            'application_service': create_account_application_service()
        }
    )

    api.add_resource(
        AccountControllerById,
        '/v1/accounts/<int:account_id>',
        resource_class_kwargs={
            'application_service': create_account_application_service()
        }
    )

    api.add_resource(
        AccountLockControllerById,
        '/v1/accounts/<int:account_id>/lock',
        resource_class_kwargs={
            'application_service': create_account_application_service()
        }
    )

    return api
