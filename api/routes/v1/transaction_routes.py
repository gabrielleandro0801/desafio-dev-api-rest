from flask_restful import Api

from api.controllers.v1.factories import create_transaction_validator, create_transaction_application_service
from api.controllers.v1.transaction_controller import TransactionController


def add_routes(api: Api) -> Api:
    api.add_resource(
        TransactionController,
        '/v1/transactions',
        resource_class_kwargs={
            'transaction_validator': create_transaction_validator(),
            'application_service': create_transaction_application_service()
        }
    )
    return api
