import flask_restful as fr

from src.application.application_service import ApplicationService
from src.controllers.v1.accounts_controller import AccountsController, AccountsControllerById, \
    AccountsLockControllerById
from src.controllers.validators.accounts_validator import AccountsValidator
from src.domain.services.accounts_service import AccountsService
from src.domain.services.users_service import UsersService
from src.domain.validators.account_status_validator import AccountStatusValidator
from src.infrastructure.database.repositories.accounts_repository import AccountsRepository
from src.infrastructure.database.repositories.users_repository import UsersRepository
from src.infrastructure.translators.accounts_translator import AccountsTranslator
from src.infrastructure.translators.transactions_translator import TransactionsTranslator
from src.infrastructure.translators.users_translator import UsersTranslator


def add_routes(api: fr.Api) -> fr.Api:
    api.add_resource(
        AccountsController,
        '/v1/accounts',
        resource_class_kwargs={
            'accounts_validator': AccountsValidator,
            'application_service': ApplicationService(
                users_service=UsersService(
                    users_translator=UsersTranslator,
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

    api.add_resource(
        AccountsControllerById,
        '/v1/accounts/<account_id>',
        resource_class_kwargs={
            'application_service': ApplicationService(
                users_service=UsersService(
                    users_repository=UsersRepository
                ),
                accounts_service=AccountsService(
                    accounts_repository=AccountsRepository,
                    accounts_translator=AccountsTranslator
                )
            )
        }
    )

    api.add_resource(
        AccountsLockControllerById,
        '/v1/accounts/<account_id>/lock',
        resource_class_kwargs={
            'application_service': ApplicationService(
                users_service=UsersService(
                    users_repository=UsersRepository
                ),
                accounts_service=AccountsService(
                    accounts_repository=AccountsRepository,
                    accounts_translator=AccountsTranslator
                )
            )
        }
    )

    return api
