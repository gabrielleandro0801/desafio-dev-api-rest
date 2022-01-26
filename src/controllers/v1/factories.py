from src.application.application_service import ApplicationService
from src.controllers.validators.accounts_validator import AccountsValidator
from src.controllers.validators.transactions_validator import TransactionsValidator
from src.controllers.validators.users_validator import UsersValidator


def create_user_validator() -> UsersValidator:
    from validate_docbr import CPF, CNPJ
    from src.controllers.validators.types_validator import StringValidator
    from src.controllers.validators.document_validator import DocumentValidator

    return UsersValidator(
        documents_validator=DocumentValidator(
            cpf_validator=CPF(),
            cnpj_validator=CNPJ()
        ),
        string_validator=StringValidator
    )


def create_accounts_validator() -> AccountsValidator:
    from src.controllers.validators.types_validator import IntValidator

    return AccountsValidator(
        int_validator=IntValidator
    )


def create_transactions_validator() -> TransactionsValidator:
    from src.controllers.validators.types_validator import FloatValidator, IntValidator, DateValidator
    from src.domain.models.transactions import TransactionTypes

    return TransactionsValidator(
        transaction_types=TransactionTypes,
        float_validator=FloatValidator,
        int_validator=IntValidator,
        date_validator=DateValidator
    )


def create_application_service() -> ApplicationService:
    from src.domain.services.accounts_service import AccountsService
    from src.domain.services.transactions_service import TransactionsService
    from src.domain.services.users_service import UsersService
    from src.domain.validators.account_status_validator import AccountStatusValidator
    from src.infrastructure.database.repositories.accounts_repository import AccountsRepository
    from src.infrastructure.database.repositories.transactions_repository import TransactionsRepository
    from src.infrastructure.database.repositories.users_repository import UsersRepository
    from src.infrastructure.translators.accounts_translator import AccountsTranslator
    from src.infrastructure.translators.transactions_translator import TransactionsTranslator

    return ApplicationService(
        users_service=UsersService(
            users_repository=UsersRepository
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
