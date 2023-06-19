import pytest

from http import HTTPStatus

from base.api.character_api import get_characters_api
from base.api.reset_api import post_reset_api
from utils.assertions.solutions import assert_status_code
from utils.constants import BASE_RESET_LENGTH


@pytest.mark.reset
def test_reset_authorized():
    '''Тест сброса системы (авторизованный).
    Проверяет, что при авторизованном сбросе системы получен корректный статус код OK.
    Затем проверяет, что размер базы данных персонажей после сброса равен ожидаемому значению BASE_RESET_LENGTH.'''
    response = post_reset_api(auth=True)

    assert_status_code(response.status_code, HTTPStatus.OK)

    base_length = len(get_characters_api(auth=True).json()['result'])

    assert base_length == BASE_RESET_LENGTH, f'База не обнулилась, её размер по-прежнему {base_length}'


@pytest.mark.reset
def test_reset_unauthorized():
    '''Тест сброса системы (неавторизованный).
    Проверяет, что при неавторизованном сбросе системы получен корректный статус код UNAUTHORIZED.'''
    response = post_reset_api()

    assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)
