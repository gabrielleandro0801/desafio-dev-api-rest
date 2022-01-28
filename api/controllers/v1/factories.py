from api.application.application_service import ApplicationService
from api.controllers.validators.accounts_validator import AccountsValidator
from api.controllers.validators.transactions_validator import TransactionsValidator
from api.controllers.validators.users_validator import UsersValidator


def create_user_validator() -> UsersValidator:
    from validate_docbr import CPF, CNPJ
    from api.controllers.validators.types_validator import StringValidator
    from api.controllers.validators.document_validator import DocumentValidator

    return UsersValidator(
        documents_validator=DocumentValidator(
            cpf_validator=CPF(),
            cnpj_validator=CNPJ()
        ),
        string_validator=StringValidator
    )


def create_accounts_validator() -> AccountsValidator:
    from api.controllers.validators.types_validator import IntValidator

    return AccountsValidator(
        int_validator=IntValidator
    )


def create_transactions_validator() -> TransactionsValidator:
    from api.controllers.validators.types_validator import FloatValidator, IntValidator, DateValidator
    from api.domain.models.transactions import TransactionTypes

    return TransactionsValidator(
        transaction_types=TransactionTypes,
        float_validator=FloatValidator,
        int_validator=IntValidator,
        date_validator=DateValidator
    )


def create_application_service() -> ApplicationService:
    from api.domain.services.accounts_service import AccountsService
    from api.domain.services.transactions_service import TransactionsService
    from api.domain.services.users_service import UsersService
    from api.domain.validators.account_status_validator import AccountStatusValidator
    from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
    from api.infrastructure.database.repositories.transactions_repository import TransactionsRepository
    from api.infrastructure.database.repositories.users_repository import UsersRepository
    from api.infrastructure.translators.accounts_translator import AccountsTranslator
    from api.infrastructure.translators.transactions_translator import TransactionsTranslator
    from api.infrastructure.translators.users_translator import UsersTranslator

    return ApplicationService(
        users_service=UsersService(
            users_repository=UsersRepository,
            users_translator=UsersTranslator
        ),
        accounts_service=AccountsService(
            accounts_repository=AccountsRepository,
            accounts_translator=AccountsTranslator
        ),
        transactions_service=TransactionsService(
            transactions_repository=TransactionsRepository,
            transactions_translator=TransactionsTranslator
        ),
        account_status_validator=AccountStatusValidator
    )
