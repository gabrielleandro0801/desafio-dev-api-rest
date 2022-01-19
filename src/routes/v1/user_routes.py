import flask_restful as fr
from validate_docbr import CPF, CNPJ

from src.application.application_service import ApplicationService
from src.controllers.v1.users.users_controller import UsersController, UsersControllerById
from src.controllers.validators.document_validator import DocumentValidator
from src.controllers.validators.string_validator import StringValidator
from src.controllers.validators.users_validator import UsersValidator
from src.domain.services.users_service import UsersService
from src.infrastructure.database.repositories.users_repository import UsersRepository
from src.infrastructure.translators.users_translator import UsersTranslator


def add_routes(api: fr.Api) -> fr.Api:
    api.add_resource(
        UsersController,
        '/v1/users',
        resource_class_kwargs={
            'users_validator': UsersValidator(
                documents_validator=DocumentValidator(
                    cpf_validator=CPF(),
                    cnpj_validator=CNPJ()
                ),
                string_validator=StringValidator
            ),
            'application_service': ApplicationService(
                users_service=UsersService(
                    users_repository=UsersRepository()
                ),
                users_translator=UsersTranslator()
            )
        }
    )

    api.add_resource(
        UsersControllerById,
        '/v1/users/<bank_number>',
        resource_class_kwargs={

        }
    )
    return api
