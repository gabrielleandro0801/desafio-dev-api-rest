class DocumentAlreadyExists(Exception):
    def __init__(self):
        super().__init__('DocumentAlreadyExists')


class UserNotFound(Exception):
    def __init__(self):
        super().__init__('UserNotFound')


class AccountAlreadyExists(Exception):
    def __init__(self):
        super().__init__('AccountAlreadyExists')


class AccountNotFound(Exception):
    def __init__(self):
        super().__init__('AccountNotFound')


class AccountStatusDoesNotAllowToClose(Exception):
    def __init__(self):
        super().__init__('AccountStatusDoesNotAllowToClose')
