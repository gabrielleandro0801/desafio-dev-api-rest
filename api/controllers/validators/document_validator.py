from abc import ABC, abstractmethod


class DocumentValidator:
    def __init__(self, cpf_validator, cnpj_validator) -> None:
        self.__cpf_validator: CPFValidator = cpf_validator
        self.__cnpj_validator: CNPJValidator = cnpj_validator

    def validate_document(self, document: str) -> str:
        doc_types: dict = {
            '11': self.__cpf_validator.validate,
            '14': self.__cnpj_validator.validate
        }

        doc_length: str = str(len(document))
        if doc_length not in doc_types:
            raise Exception

        is_valid: bool = doc_types[doc_length](document)
        if not is_valid:
            raise Exception

        return document


class Validator(ABC):
    @abstractmethod
    def validate(self, document: str) -> bool:
        pass


class CPFValidator(Validator):
    def __init__(self, validator) -> None:
        self.__validator = validator

    def validate(self, document: str) -> bool:
        return self.__validator.validate(document)


class CNPJValidator(Validator):
    def __init__(self, validator) -> None:
        self.__validator = validator

    def validate(self, document: str) -> bool:
        return self.__validator.validate(document)
