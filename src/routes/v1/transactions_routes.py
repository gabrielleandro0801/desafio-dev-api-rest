from flask_restful import Api

from src.application.application_service import ApplicationService
from src.controllers.v1.transactions_controller import TransactionsController
from src.controllers.validators.transactions_validator import TransactionsValidator
from src.domain.models.transactions import TransactionTypes
from src.domain.services.accounts_service import AccountsService
from src.domain.services.users_service import UsersService
from src.domain.validators.account_status_validator import AccountStatusValidator
from src.infrastructure.database.repositories.accounts_repository import AccountsRepository
from src.infrastructure.database.repositories.users_repository import UsersRepository
from src.infrastructure.translators.accounts_translator import AccountsTranslator
from src.infrastructure.translators.transactions_translator import TransactionsTranslator


def add_routes(api: Api) -> Api:
    api.add_resource(
        TransactionsController,
        '/v1/transactions',
        resource_class_kwargs={
            'transactions_validator': TransactionsValidator(
                transaction_types=TransactionTypes
            ),
            'application_service': ApplicationService(
                users_service=UsersService(
                    users_repository=UsersRepository
                ),
                accounts_service=AccountsService(
                    accounts_repository=AccountsRepository,
                    accounts_translator=AccountsTranslator
                ),
                transactions_translator=TransactionsTranslator,
                account_status_validator=AccountStatusValidator
            )
        }
    )
    return api
