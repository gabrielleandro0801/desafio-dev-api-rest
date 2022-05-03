class DocumentAlreadyExists(Exception):
    def __init__(self):
        super().__init__('DocumentAlreadyExists')


class UserNotFound(Exception):
    def __init__(self):
        super().__init__('UserNotFound')


class UserHasAccount(Exception):
    def __init__(self):
        super().__init__('UserHasAccount')


class AccountAlreadyExists(Exception):
    def __init__(self):
        super().__init__('AccountAlreadyExists')


class AccountNotFound(Exception):
    def __init__(self):
        super().__init__('AccountNotFound')


class AccountStatusDoesNotAllowToClose(Exception):
    def __init__(self):
        super().__init__('AccountStatusDoesNotAllowToClose')


class AccountStatusDoesNotAllowToLock(Exception):
    def __init__(self):
        super().__init__('AccountStatusDoesNotAllowToLock')


class AccountStatusDoesNotAllowToUnLock(Exception):
    def __init__(self):
        super().__init__('AccountStatusDoesNotAllowToUnLock')


class AccountStatusDoesNotAllowToTransact(Exception):
    def __init__(self):
        super().__init__('AccountStatusDoesNotAllowToTransact')


class AccountStatusDoesNotAllowToListTransactions(Exception):
    def __init__(self):
        super().__init__('AccountStatusDoesNotAllowToListTransactions')


class AccountHasNoEnoughBalance(Exception):
    def __init__(self):
        super().__init__('AccountHasNoEnoughBalance')


class WithdrawSurpassesDailyLimitBalance(Exception):
    def __init__(self):
        super().__init__('WithdrawSurpassesDailyLimitBalance')
