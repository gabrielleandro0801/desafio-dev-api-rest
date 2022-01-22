import src.domain.models.accounts as a
import src.domain.models.users as u

from src.infrastructure.database.repositories import accounts_repository as ar
from src.infrastructure.translators.accounts_translator import AccountsTranslator


class AccountsService:
    def __init__(self, **kwargs):
        self.__accounts_repository: ar.AccountsRepository = kwargs.get('accounts_repository')
        self.__accounts_translator: AccountsTranslator = kwargs.get('accounts_translator')

    def get_account(self, account_id: int) -> a.Accounts or None:
        return self.__accounts_repository.find_by_account_id(account_id)

    def create_account(self, user: u.Users) -> a.Accounts:
        account: a.Accounts = self.__accounts_translator.translate_account_to_create(user)
        return self.__accounts_repository.create_account(account)

    def close_account(self, account: a.Accounts) -> None:
        self.__accounts_repository.close_account(account)

    def lock_account(self, account: a.Accounts) -> None:
        self.__accounts_repository.update_status(account, 'LOCKED')

    def unlock_account(self, account: a.Accounts) -> None:
        self.__accounts_repository.update_status(account, 'ACTIVE')

    def get_existing_account_by_user_id(self, user_id: int) -> bool:
        existing_account: a.Accounts = self.__accounts_repository.find_by_user_id_and_status(user_id,
                                                                                             a.EXISTING_ACCOUNT_STATUS)
        return True if existing_account is not None else False

    def update_balance(self, account: a.Accounts, amount: float, operation: str) -> None:
        from src.domain.models.transactions import TransactionTypes

        if operation == TransactionTypes.DEPOSIT:
            current_balance = account.balance + amount
        else:
            current_balance = account.balance - amount

        self.__accounts_repository.update_balance(account, current_balance)
