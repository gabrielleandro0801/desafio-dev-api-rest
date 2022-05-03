from api.domain.models.account import Account, AccountStatus, EXISTING_ACCOUNT_STATUS
from api.domain.models.user import User
from api.infrastructure.database.repositories.accounts_repository import AccountsRepository
from api.infrastructure.translators.account_translator import AccountTranslator


class AccountService:
    def __init__(self, **kwargs):
        self.__accounts_repository: AccountsRepository = kwargs.get('accounts_repository')
        self.__account_translator: AccountTranslator = kwargs.get('account_translator')

    def create_account(self, user: User) -> Account:
        account: Account = self.__account_translator.translate_account_to_create(user)
        return self.__accounts_repository.create_account(account)

    def lock_account(self, account: Account) -> None:
        self.__accounts_repository.update_status(account, AccountStatus.LOCKED)

    def unlock_account(self, account: Account) -> None:
        self.__accounts_repository.update_status(account, AccountStatus.ACTIVE)

    def retrieve_existing_account_by_user_id(self, user_id: int) -> bool:
        existing_account: Account = self.__accounts_repository.find_by_user_id_and_status(user_id,
                                                                                          EXISTING_ACCOUNT_STATUS)
        return True if existing_account is not None else False

    def update_balance(self, account: Account, amount: float, operation: str) -> None:
        from api.domain.models.transaction import TransactionTypes

        new_balance = account.balance + amount if operation == TransactionTypes.DEPOSIT else account.balance - amount
        self.__accounts_repository.update_balance(account, new_balance)
