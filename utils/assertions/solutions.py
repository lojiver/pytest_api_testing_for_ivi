from http import HTTPStatus
from jsonschema import validate


def assert_status_code(actual: int, expected: HTTPStatus) -> None:
    '''Проверяет соответствие фактического статус-кода с ожидаемым статус-кодом.

    Аргументы:
    - actual (int): Фактический статус-код.
    - expected (HTTPStatus): Ожидаемый статус-код из модуля `http`.

    Если фактический статус-код не совпадает с ожидаемым, генерируется AssertionError
    с информацией о несоответствии.'''
    assert actual == expected, f'Ожидается статус-код {expected}, пришёл статус-код {actual}'


def validate_schema(instance: dict, schema: dict) -> None:
    '''Проверяет соответствие данных `instance` с заданным схемой `schema`.

    Аргументы:
    - instance (dict): Данные для проверки соответствия схеме.
    - schema (dict): Схема, с которой сравниваются данные.

    Функция использует библиотеку `jsonschema` для проверки соответствия данных схеме.
    Если данные не соответствуют схеме, генерируется `ValidationError`.'''
    validate(instance=instance, schema=schema)


def validate_error_text(expected_error: str, response_text: str) -> None:
    '''Проверяет наличие ожидаемого текста ошибки в тексте ответа.

    Аргументы:
    - expected_error (str): Ожидаемый текст ошибки.
    - response_text (str): Текст ответа, в котором проверяется наличие ожидаемого текста ошибки.

    Если ожидаемый текст ошибки не найден в тексте ответа, генерируется AssertionError
    с информацией о несоответствии.'''
    assert expected_error in response_text, f'В ответе нет текст ошибки {expected_error}'
