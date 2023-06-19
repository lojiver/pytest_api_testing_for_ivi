from requests import Response

from base.client import get_client
from utils.models.character import Character
from utils.constants import APIRoutes


def get_characters_api(auth: bool = False) -> Response:
    '''Выполняет GET-запрос для получения списка персонажей.

    Args:
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Response: Ответ сервера.'''
    client = get_client(auth=auth)
    return client.get(url=APIRoutes.CHARACTERS)


def get_character_api(character_name: str, auth: bool = False) -> Response:
    '''Выполняет GET-запрос для получения информации о конкретном персонаже.

    Args:
        character_name (str): Имя персонажа.
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Response: Ответ сервера'''
    client = get_client(auth=auth)
    params = {'name': character_name}
    return client.get(f'{APIRoutes.CHARACTER}', params=params)


def create_character_api(payload: dict, auth: bool = False) -> Response:
    '''Выполняет POST-запрос для создания нового персонажа.

    Args:
        payload (dict): Данные о персонаже.
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Response: Ответ сервера.'''
    client = get_client(auth=auth)
    return client.post(APIRoutes.CHARACTER, json=payload)


def update_character_api(payload: dict, auth: bool = False) -> Response:
    '''Выполняет PUT-запрос для обновления данных персонажа.

    Args:
        payload (dict): Новые данные о персонаже.
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Response: Ответ сервера.'''
    client = get_client(auth=auth)
    return client.put(f'{APIRoutes.CHARACTER}', json=payload)


def delete_character_api(character_name: str, auth: bool = False) -> Response:
    '''Выполняет DELETE-запрос для удаления персонажа.

    Args:
        character_name (str): Имя персонажа.
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Response: Ответ сервера.'''
    client = get_client(auth=auth)
    params = {'name': character_name}
    return client.delete(f'{APIRoutes.CHARACTER}', params=params)


def create_character(auth: bool = False) -> Character:
    '''Создает нового персонажа.

    Args:
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Character: Созданный персонаж.'''
    payload = Character()

    response = create_character_api(payload=payload.dict(), auth=auth)
    return Character(**response.json()['result'])
