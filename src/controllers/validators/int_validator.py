class IntValidator:

    @classmethod
    def validate(cls, value: int) -> int:
        if type(value) is not int:
            raise Exception

        if value <= 0:
            raise Exception

        return value
