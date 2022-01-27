from api.domain.models.accounts import Accounts, AccountsStatus
from api.domain.models.users import Users


class AccountsTranslator:

    @classmethod
    def translate_account_to_create(cls, user: Users) -> Accounts:
        DEFAULT_BANK_BRANCH: str = '0001'
        DEFAULT_WITHDRAW_LIMIT: int = 2000
        DEFAULT_ZERO_BALANCE: int = 0

        return Accounts(
            status=AccountsStatus.ACTIVE,
            number=AccountsTranslator.create_account_number(user.id, user.document),
            bank_branch=DEFAULT_BANK_BRANCH,
            balance=DEFAULT_ZERO_BALANCE,
            withdraw_daily_limit=DEFAULT_WITHDRAW_LIMIT,
            user_id=user.id
        )

    @classmethod
    def create_account_number(cls, user_id: int, doc: str) -> int:
        return int(f'{doc[0:5]}{user_id}')
