from flask_restful import Api

from api.controllers.v1.factories import create_transactions_validator, create_transactions_application_service
from api.controllers.v1.transactions_controller import TransactionsController


def add_routes(api: Api) -> Api:
    api.add_resource(
        TransactionsController,
        '/v1/transactions',
        resource_class_kwargs={
            'transactions_validator': create_transactions_validator(),
            'application_service': create_transactions_application_service()
        }
    )
    return api
