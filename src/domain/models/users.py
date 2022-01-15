class Users:
    def __init__(self, **kwargs) -> None:
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name')
        self.__document = kwargs.get('document')

    def to_json(self) -> dict:
        return {
            'name': self.__name,
            'document': self.__document
        }
