class FloatValidator:

    @classmethod
    def validate(cls, value: float) -> float:
        if type(value) not in [float, int]:
            raise Exception

        if value <= 0:
            raise Exception

        return value


class IntValidator:

    @classmethod
    def validate(cls, value: int) -> int:
        try:
            value = int(value)
        except ValueError:
            raise Exception

        if type(value) is not int:
            raise Exception

        if value <= 0:
            raise Exception

        return value


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


class DateValidator:

    @classmethod
    def validate(cls, value: str):
        import re

        basic_iso8061_regex: str = '^(-?(?:[1-9][0-9]*)?[0-9]{4})-' \
                                   '(1[0-2]|0[1-9])-' \
                                   '(3[01]|0[1-9]|[12][0-9])'

        full_iso8061_regex: str = '^(-?(?:[1-9][0-9]*)?[0-9]{4})-' \
                                  '(1[0-2]|0[1-9])-' \
                                  '(3[01]|0[1-9]|[12][0-9])T' \
                                  '(2[0-3]|[01][0-9]):' \
                                  '([0-5][0-9]):' \
                                  '([0-5][0-9])(\.[0-9]+)' \
                                  '?(Z|[+-](?:2[0-3]|[01][0-9])' \
                                  ':[0-5][0-9])?$'

        match_iso8601 = re.compile(full_iso8061_regex).match
        if match_iso8601(value) is not None:
            return value

        match_iso8601 = re.compile(basic_iso8061_regex).fullmatch
        if match_iso8601(value) is not None:
            return value
        raise Exception
