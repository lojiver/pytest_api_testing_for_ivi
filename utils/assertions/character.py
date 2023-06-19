from utils.models.character import CharacterDict, Character


def assert_character(expected_character: CharacterDict, actual_character: Character):
    '''Проверяет соответствие полей персонажа в соответствии с ожидаемыми значениями.

    Аргументы:
    - expected_character (CharacterDict): Ожидаемые значения полей персонажа в виде словаря.
    - actual_character (Character): Фактические значения полей персонажа в виде объекта Character.

    Проверяется соответствие типов значений полей и их фактических значений с ожидаемыми.
    Если типы или значения не совпадают, генерируется AssertionError с информацией о несоответствии.'''
    expected_character = expected_character.dict()
    # поскольку большинство полей необязательные,
    # используем цикл по имеющимся полям каждого конкретного полученного объекта
    for key, value in actual_character.items():
        expected_type = type(expected_character[key])
        assert isinstance(value, expected_type), (f'Поле {key} должно быть {expected_type}, а его тип {type(value)}')

        assert value == expected_character[key], (
            f'Поле {key} не совпадает, ожидаемое значение {expected_character[key]},' +
            f'полученное значение {value}')
