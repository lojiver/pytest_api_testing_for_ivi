import pytest

from base.api.character_api import create_character, delete_character_api, get_characters_api
from base.api.reset_api import post_reset_api
from utils.constants import BASE_LIMIT
from utils.models.character import Character


@pytest.fixture(scope='function')
def function_character() -> Character:
    '''Фикстура, предоставляющая объект персонажа для тестов.

    Создает нового персонажа с помощью функции `create_character` с авторизацией.
    Возвращает созданного персонажа.
    После выполнения тестов удаляет созданного персонажа с помощью функции `delete_character_api`.

    Возвращает:
    - Character: Объект персонажа для тестов.'''
    character = create_character(auth=True)
    yield character

    delete_character_api(character.name, auth=True)


@pytest.fixture(scope='function')
def fill_base_to_full() -> None:
    '''Фикстура, заполняющая базу персонажей до максимального предела.

    Проверяет текущую полноту базы персонажей с помощью функции `get_characters_api`.
    Рассчитывает количество недостающих персонажей для заполнения базы до предела.
    Создает недостающих персонажей с помощью функции `create_character` с авторизацией.
    После выполнения тестов сбрасывает базу персонажей с помощью функции `post_reset_api` с авторизацией.

    Возвращает:
    - None'''
    base_fullness = len(get_characters_api(auth=True).json()['result'])
    empty_space = BASE_LIMIT - base_fullness
    for i in range(empty_space):
        create_character(auth=True)
    yield

    post_reset_api(auth=True)
