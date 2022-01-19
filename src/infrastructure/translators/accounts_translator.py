import src.domain.models.accounts as a
import src.domain.models.users as u


class AccountsTranslator:
    def __init__(self):
        pass

    @classmethod
    def translate_account_to_create(cls, user: u.Users) -> a.Accounts:
        DEFAULT_BANK_BRANCH: str = '0001'
        DEFAULT_WITHDRAW_LIMIT: int = 2000
        DEFAULT_ZERO_BALANCE: int = 0

        return a.Accounts(
            status='ACTIVE',
            number=AccountsTranslator.create_account_number(user.id, user.document),
            bank_branch=DEFAULT_BANK_BRANCH,
            balance=DEFAULT_ZERO_BALANCE,
            withdraw_daily_limit=DEFAULT_WITHDRAW_LIMIT,
            user_id=user.id
        )

    @classmethod
    def create_account_number(cls, user_id: int, doc: str) -> int:
        return int(f'{doc[0:5]}{user_id}')
