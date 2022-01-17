from flask_restful import Api
from validate_docbr import CPF, CNPJ

from src.application.application_service import ApplicationService
from src.controllers.v1.users.users_controller import UsersController
from src.controllers.validators.document_validator import DocumentValidator
from src.controllers.validators.users_validator import UsersValidator
from src.infrastructure.database.repositories.users_repository import UsersRepository
from src.infrastructure.translators.users_translator import UsersTranslator


def add_routes(api: Api) -> Api:
    api.add_resource(
        UsersController,
        '/v1/users',
        resource_class_kwargs={
            'users_validator': UsersValidator(
                documents_validator=DocumentValidator(
                    cpf_validator=CPF(),
                    cnpj_validator=CNPJ()
                )
            ),
            'application_service': ApplicationService(
                users_repository=UsersRepository(),
                users_translator=UsersTranslator()
            )
        }
    )
    return api
