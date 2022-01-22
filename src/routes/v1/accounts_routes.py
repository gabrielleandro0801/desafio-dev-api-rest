from flask_restful import Api

from src.controllers.v1.accounts_controller import AccountsController, AccountsControllerById, \
    AccountsLockControllerById
from src.controllers.v1.factories import create_application_service, create_accounts_validator


def add_routes(api: Api) -> Api:
    api.add_resource(
        AccountsController,
        '/v1/accounts',
        resource_class_kwargs={
            'accounts_validator': create_accounts_validator(),
            'application_service': create_application_service()
        }
    )

    api.add_resource(
        AccountsControllerById,
        '/v1/accounts/<account_id>',
        resource_class_kwargs={
            'application_service': create_application_service()
        }
    )

    api.add_resource(
        AccountsLockControllerById,
        '/v1/accounts/<account_id>/lock',
        resource_class_kwargs={
            'application_service': create_application_service()
        }
    )

    return api
