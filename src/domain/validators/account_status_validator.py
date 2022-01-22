from src.domain.models.accounts import AccountsStatus


class AccountStatusValidator:

    @classmethod
    def validate_status_to_do_transaction(cls, status: str) -> bool:
        return True if status == AccountsStatus.ACTIVE else False

    @classmethod
    def validate_status_to_lock_account(cls, status: str):
        return True if status == AccountsStatus.ACTIVE else False

    @classmethod
    def validate_status_to_unlock_account(cls, status: str):
        return True if status == AccountsStatus.LOCKED else False

    @classmethod
    def validate_status_to_close_account(cls, status: str):
        return True if status == AccountsStatus.ACTIVE else False
