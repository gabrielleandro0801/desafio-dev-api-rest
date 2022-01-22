import src.domain.exceptions.custom_exceptions as ce
import src.domain.models.accounts as a
import src.domain.models.transactions as t
import src.domain.models.users as u

from src.domain.services.accounts_service import AccountsService
from src.domain.services.users_service import UsersService
from src.domain.validators.account_status_validator import AccountStatusValidator
from src.infrastructure.translators.transactions_translator import TransactionsTranslator


class ApplicationService:
    def __init__(self, **kwargs) -> None:
        self.__users_service: UsersService = kwargs.get('users_service')
        self.__accounts_service: AccountsService = kwargs.get('accounts_service')
        self.__transactions_translator: TransactionsTranslator = kwargs.get('transactions_translator')
        self.__account_status_validator: AccountStatusValidator = kwargs.get('account_status_validator')

    def register_user(self, body: dict) -> u.Users:
        doc_already_exists: bool = self.__users_service.check_duplicated_document(body.get('document'))
        if doc_already_exists:
            raise ce.DocumentAlreadyExists

        return self.__users_service.create_user(body)

    def remove_user(self, user_id: int) -> None:
        user: u.Users = self.__users_service.get_user_by_id(user_id)
        if user is None:
            raise ce.UserNotFound

        user_has_account: bool = self.__accounts_service.get_existing_account_by_user_id(user.id)
        if user_has_account:
            raise ce.UserHasAccount

        self.__users_service.delete_user(user)

    def register_account(self, body: dict) -> a.Accounts:
        user: u.Users = self.__users_service.get_user_by_id(body.get('userId'))
        if user is None:
            raise ce.UserNotFound

        account_already_exists: bool = self.__accounts_service.get_existing_account_by_user_id(user.id)
        if account_already_exists:
            raise ce.AccountAlreadyExists

        return self.__accounts_service.create_account(user)

    def retrieve_account(self, account_id: int) -> a.Accounts:
        account: a.Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        return account

    def close_account(self, account_id: int) -> None:
        account: a.Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_close: bool = self.__account_status_validator.validate_status_to_close_account(account.status)
        if not is_able_to_close:
            raise ce.AccountStatusDoesNotAllowToClose

        self.__accounts_service.close_account(account)

    def lock_account(self, account_id: int) -> None:
        account: a.Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_lock: bool = self.__account_status_validator.validate_status_to_lock_account(account.status)
        if not is_able_to_lock:
            raise ce.AccountStatusDoesNotAllowToLock

        self.__accounts_service.lock_account(account)

    def unlock_account(self, account_id: int) -> None:
        account: a.Accounts = self.__accounts_service.get_account(account_id)
        if account is None:
            raise ce.AccountNotFound

        is_able_to_unlock: bool = self.__account_status_validator.validate_status_to_unlock_account(account.status)
        if not is_able_to_unlock:
            raise ce.AccountStatusDoesNotAllowToUnLock

        self.__accounts_service.unlock_account(account)

    def do_transaction(self, body: dict) -> None:
        from src.domain.services.transactions_service import TransactionsService

        account: a.Accounts = self.__accounts_service.get_account(body.get('accountId'))
        if account is None:
            raise ce.AccountNotFound

        is_valid: bool = self.__account_status_validator.validate_status_to_do_transaction(account.status)
        if not is_valid:
            raise ce.AccountStatusDoesNotAllowToTransact

        transaction: t.Transactions = self.__transactions_translator.translate_transaction_from_body(body)

        service: TransactionsService = self.__transactions_translator.get_operation_type(body.get('operationType'))
        service.do(transaction)

        self.__accounts_service.update_balance(account, body.get('amount'), body.get('operationType'))
