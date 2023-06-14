import pytest
import requests

from settings import name_valid_for_post, name_valid_for_get


# тесты POST /characters
def test_post_characters_new_unauthorized_request(headers, url_one_id, reset_base):
    reset_base
    json = {'name': 'Mr. Incredible', }
    response = requests.post(url_one_id, headers=headers, json=json)
    reset_base

    assert response.status_code == 401, f'Post-запрос {url_one_id} даёт добавить запись неавторизованному пользователю.'


@pytest.mark.parametrize('name', name_valid_for_get)
def test_post_characters_exists_authorized_request(auth, headers, url_one_id, reset_base, name):
    reset_base
    json = {'name': name, }
    response = requests.post(url_one_id, auth=auth, headers=headers, json=json)
    data = response.json()
    reset_base

    assert response.status_code == 400, f'БД позволяет записать персонажа с неуникальным именем {name}'
    assert data == {'error': f'{name} is already exists'}


@pytest.mark.parametrize('name', name_valid_for_post)
def test_post_characters_new_authorized_request(auth, headers, url_one_id, reset_base, name):
    reset_base
    json = {'name': name, }
    response = requests.post(url_one_id, auth=auth, headers=headers, json=json)
    data = response.json()
    reset_base

    assert response.status_code == 200, f'Ожидаемый статус-код 200, ошибка произошла на тестировании имени {name}'
    assert 'result' in data, 'В JSON-ответе нет ключа "result"'
