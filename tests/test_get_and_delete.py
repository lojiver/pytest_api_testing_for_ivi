import pytest
import requests

from settings import name_valid_for_get, name_invalid


# тесты GET /characters
def test_get_characters_authorized_request(auth, url_multi):
    response = requests.get(url_multi, auth=auth)
    data = response.json()

    assert response.status_code == 200, 'Что-то пошло не так, ожидаемый статус-код 200'
    assert 'result' in data, 'В JSON-ответе нет ключа "result"'


def test_get_characters_unauthorized_request(url_multi):
    response = requests.get(url_multi)

    assert response.status_code == 401, f'Запрос {url_multi} показывает информацию неавторизованному пользователю.'


def test_get_characters_json_keys(auth, url_multi, required_keys, expected_keys):
    response = requests.get(url_multi, auth=auth)
    data = response.json()

    for key in required_keys:
        assert key in data['result'][0], f'JSON-ответ не содержит обязательный ключ {key}'
    for key in data['result'][0]:
        assert key in expected_keys, f'Ключа {key} не ожидается в JSON_ответе'


# тесты GET /character и DELETE /character
@pytest.mark.parametrize('name', name_valid_for_get)
@pytest.mark.parametrize('request_type', [requests.get, requests.delete])
def test_get_and_delete_character_authorized_request_valid_param(auth, url_one_id, name, reset_base, request_type):
    reset_base
    params = {'name': name}
    response = request_type(url_one_id, auth=auth, params=params)
    data = response.json()
    reset_base

    assert response.status_code == 200, (
        f'Ожидаемый статус-код 200 на запрос {request_type}, ошибка произошла на тестировании имени {name}')
    assert 'result' in data, f'В JSON-ответе на запрос на запрос {request_type} нет ключа "result"'


@pytest.mark.parametrize('request_type', [requests.get, requests.delete])
def test_get_and_delete_character_unauthorized_request_valid_param(url_one_id, reset_base, request_type):
    reset_base
    params = {'name': 'Sebastian Shaw'}
    response = request_type(url_one_id, params=params)
    reset_base

    assert response.status_code == 401, (
        f'Запрос {url_one_id} типа {request_type} показывает информацию неавторизованному пользователю.')


@pytest.mark.parametrize('name', name_invalid)
@pytest.mark.parametrize('request_type', [requests.get, requests.delete])
def test_get_and_delete_character_authorized_request_invalid_param(auth, url_one_id, name, reset_base, request_type):
    reset_base
    params = {'name': name}
    response = request_type(url_one_id, auth=auth, params=params)
    reset_base

    assert response.status_code == 400, (
        f'Ожидаемый статус-код 400 в ответ на запрос {request_type}, ошибка произошла на тестировании имени {name}')
