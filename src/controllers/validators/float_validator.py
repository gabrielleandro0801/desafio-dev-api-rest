class FloatValidator:

    @classmethod
    def validate(cls, value: float) -> float:
        if type(value) not in [float, int]:
            raise Exception

        if value <= 0:
            raise Exception

        return value
