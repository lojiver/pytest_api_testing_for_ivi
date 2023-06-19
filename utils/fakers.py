from random import choice, randint, uniform
from string import ascii_letters, digits

from utils.constants import STRING_LENGTH_LIMIT


def random_float(start: float = 0.01, end: float = 999.99) -> float:
    '''Возвращает случайное число с плавающей точкой'''
    return uniform(start, end)


def random_number(start: int = 0, end: int = 1000) -> int:
    '''Возвращает случайное целое число'''
    return randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    '''Возвращает случайную строку'''
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 2, end: int = 4) -> list[str]:
    return ', '.join(random_string() for _ in range(randint(start, end)))


def injections():
    '''Значения-инъекции для тестирования негативных сценариев'''
    result = []
    result.append('nice site,  i think i\'ll take it. <script>alert("executing js")</script>')
    result.append('robert\'); drop table students;--')
    result.append('<i><b>bold</i></b>')
    result.append('"-prompt()-"')
    return result


def nulls():
    '''Отсутствующие значения для тестирования негативных сценариев'''
    return [None, '']


def invalid_string():
    '''Формирует список значений, которые можно использовать
    для тестирования негативных сценариев с типом данных "строка",
    возвращает случайное значение из списка'''
    result = []
    result.append(random_number())
    result.append(random_float())
    result.append(True)
    result.append(nulls())
    result.append(injections())
    return choice(result)


def too_long_string():
    '''Формирует строку, превышающую лимит длины строки.
    Случайным образом сделает строку длинее на 1,
    чтобы проверить краевое значение или более длинной'''
    return random_string(1, 3) * STRING_LENGTH_LIMIT + random_string(1, 1)


def invalid_float():
    '''Формирует список значений, которые можно использовать
    для тестирования негативных сценариев с типом данных "число с плавающей точкой",
    возвращает случайное значение из списка'''
    result = []
    result.append(random_number())
    result.append(random_string())
    result.append(True)
    result.append(nulls())
    result.append(injections())
    return choice(result)
