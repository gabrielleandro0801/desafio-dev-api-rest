import flask_restful as fr

from src.application.application_service import ApplicationService
from src.controllers.v1.accounts_controller import AccountsController
from src.controllers.validators.accounts_validator import AccountsValidator
from src.domain.services.accounts_service import AccountsService
from src.domain.services.users_service import UsersService
from src.infrastructure.database.repositories.accounts_repository import AccountsRepository
from src.infrastructure.database.repositories.users_repository import UsersRepository
from src.infrastructure.translators.accounts_translator import AccountsTranslator
from src.infrastructure.translators.users_translator import UsersTranslator


def add_routes(api: fr.Api) -> fr.Api:
    api.add_resource(
        AccountsController,
        '/v1/accounts',
        resource_class_kwargs={
            'accounts_validator': AccountsValidator(),
            'application_service': ApplicationService(
                users_service=UsersService(
                    users_repository=UsersRepository
                ),
                users_translator=UsersTranslator(),
                accounts_service=AccountsService(
                    accounts_repository=AccountsRepository,
                    accounts_translator=AccountsTranslator
                )
            )
        }
    )

    return api
