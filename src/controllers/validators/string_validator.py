class StringValidator:

    @classmethod
    def str_validation(cls, max_length=None):
        def validate(string: str) -> str:
            if type(string) is not str:
                raise Exception

            if len(string) == 0:
                raise Exception

            if max_length is not None:
                if len(string) > max_length:
                    raise Exception

            return string
        return validate
