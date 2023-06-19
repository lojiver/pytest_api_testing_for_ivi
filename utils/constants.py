from enum import Enum

BASE_LIMIT = 500
BASE_RESET_LENGTH = 302
STRING_LENGTH_LIMIT = 350


class Errors(str, Enum):
    '''Список ожидаемых тектов ошибок'''
    NO_REQUIRED_FIELD = 'Missing data for required field.'
    NOT_VALID_VALUE = 'Not a valid'
    ALREADY_EXISTS = 'is already exists'
    FULL_BASE = f'Collection can\'t contain more than {BASE_LIMIT} items'
    NO_SUCH_NAME = 'No such name'
    TOO_LONG = f'Length must be between 1 and {STRING_LENGTH_LIMIT}.'

    def __str__(self) -> str:
        return self.value


class APIRoutes(str, Enum):
    '''Список эндпоинтов API'''
    CHARACTER = '/character'
    CHARACTERS = '/characters'
    RESET = '/reset'

    def __str__(self) -> str:
        return self.value
