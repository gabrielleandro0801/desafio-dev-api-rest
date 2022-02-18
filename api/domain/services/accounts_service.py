from api.domain.models.accounts import Accounts, AccountsStatus, EXISTING_ACCOUNT_STATUS
from api.domain.models.users import Users
from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
from api.infrastructure.translators.accounts_translator import AccountsTranslator


class AccountsService:
    def __init__(self, **kwargs):
        self.__accounts_repository: AccountsRepository = kwargs.get('accounts_repository')
        self.__accounts_translator: AccountsTranslator = kwargs.get('accounts_translator')

    def create_account(self, user: Users) -> Accounts:
        account: Accounts = self.__accounts_translator.translate_account_to_create(user)
        return self.__accounts_repository.create_account(account)

    def lock_account(self, account: Accounts) -> None:
        self.__accounts_repository.update_status(account, AccountsStatus.LOCKED)

    def unlock_account(self, account: Accounts) -> None:
        self.__accounts_repository.update_status(account, AccountsStatus.ACTIVE)

    def retrieve_existing_account_by_user_id(self, user_id: int) -> bool:
        existing_account: Accounts = self.__accounts_repository.find_by_user_id_and_status(user_id,
                                                                                           EXISTING_ACCOUNT_STATUS)
        return True if existing_account is not None else False

    def update_balance(self, account: Accounts, amount: float, operation: str) -> None:
        from api.domain.models.transactions import TransactionTypes

        if operation == TransactionTypes.DEPOSIT:
            current_balance = account.balance + amount
        else:
            current_balance = account.balance - amount

        self.__accounts_repository.update_balance(account, current_balance)
