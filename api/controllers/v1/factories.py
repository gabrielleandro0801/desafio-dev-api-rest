from api.application.account_application_service import AccountApplicationService
from api.application.transaction_application_service import TransactionApplicationService
from api.application.user_application_service import UserApplicationService

from api.controllers.validators.account_validator import AccountValidator
from api.controllers.validators.transaction_validator import TransactionValidator
from api.controllers.validators.user_validator import UserValidator


def create_user_validator() -> UserValidator:
    from validate_docbr import CPF, CNPJ
    from api.controllers.validators.types_validator import StringValidator
    from api.controllers.validators.document_validator import DocumentValidator

    return UserValidator(
        document_validator=DocumentValidator(
            cpf_validator=CPF(),
            cnpj_validator=CNPJ()
        ),
        string_validator=StringValidator
    )


def create_account_validator() -> AccountValidator:
    from api.controllers.validators.types_validator import IntValidator

    return AccountValidator(
        int_validator=IntValidator
    )


def create_transaction_validator() -> TransactionValidator:
    from api.controllers.validators.types_validator import FloatValidator, IntValidator, DateValidator
    from api.domain.models.transaction import TransactionTypes

    return TransactionValidator(
        transaction_types=TransactionTypes,
        float_validator=FloatValidator,
        int_validator=IntValidator,
        date_validator=DateValidator
    )


def create_user_application_service() -> UserApplicationService:
    from api.domain.services.account_service import AccountService
    from api.domain.services.user_service import UserService
    from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
    from api.infrastructure.database.repositories.users_repository import UsersRepository
    from api.infrastructure.translators.account_translator import AccountTranslator
    from api.infrastructure.translators.user_translator import UserTranslator

    return UserApplicationService(
        user_service=UserService(
            users_repository=UsersRepository,
            user_translator=UserTranslator
        ),
        users_repository=UsersRepository,
        account_service=AccountService(
            accounts_repository=AccountsRepository,
            account_translator=AccountTranslator
        )
    )


def create_account_application_service() -> AccountApplicationService:
    from api.domain.services.account_service import AccountService
    from api.domain.validators.account_status_validator import AccountStatusValidator
    from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
    from api.infrastructure.database.repositories.users_repository import UsersRepository
    from api.infrastructure.translators.account_translator import AccountTranslator

    return AccountApplicationService(
        users_repository=UsersRepository,
        accounts_repository=AccountsRepository,
        account_service=AccountService(
            accounts_repository=AccountsRepository,
            account_translator=AccountTranslator
        ),
        account_status_validator=AccountStatusValidator
    )


def create_transaction_application_service() -> TransactionApplicationService:
    from api.domain.services.account_service import AccountService
    from api.domain.services.transaction_service import TransactionService
    from api.domain.validators.account_status_validator import AccountStatusValidator
    from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
    from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository
    from api.infrastructure.translators.account_translator import AccountTranslator
    from api.infrastructure.translators.transaction_translator import TransactionTranslator

    return TransactionApplicationService(
        account_status_validator=AccountStatusValidator,
        account_service=AccountService(
            accounts_repository=AccountsRepository,
            account_translator=AccountTranslator
        ),
        accounts_repository=AccountsRepository,
        transaction_service=TransactionService(
            transaction_translator=TransactionTranslator
        ),
        transactions_repository=TransactionsRepository
    )
