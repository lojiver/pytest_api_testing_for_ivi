import requests

from functools import lru_cache

from settings import base_settings


class Client:
    def __init__(self, auth=None):
        '''Класс для клиента API.

        Args:
            auth: Аутентификационные данные (по умолчанию None).'''
        self.auth = auth
        # здесь базовый URL из базовых настроек
        self.base_url = base_settings.api_url

    def get(self, url, *args, **kwargs) -> requests.Response:
        '''Выполняет GET-запрос.

        Args:
            url: URL запроса.
            *args: Позиционные аргументы для requests.get.
            **kwargs: Именованные аргументы для requests.get.

        Returns:
            requests.Response: Ответ сервера на GET-запрос.'''
        return requests.get(auth=self.auth, url=self.base_url + url, *args, **kwargs)

    def post(self, url, *args, **kwargs) -> requests.Response:
        '''Выполняет POST-запрос.

        Args:
            url: URL запроса.
            *args: Позиционные аргументы для requests.post.
            **kwargs: Именованные аргументы для requests.post.

        Returns:
            requests.Response: Ответ сервера на POST-запрос.'''
        return requests.post(auth=self.auth, url=self.base_url + url, *args, **kwargs)

    def put(self, url, *args, **kwargs) -> requests.Response:
        '''Выполняет PUT-запрос.

        Args:
            url: URL запроса.
            *args: Позиционные аргументы для requests.put.
            **kwargs: Именованные аргументы для requests.put.

        Returns:
            requests.Response: Ответ сервера на PUT-запрос.'''
        return requests.put(auth=self.auth, url=self.base_url + url, *args, **kwargs)

    def delete(self, url, *args, **kwargs) -> requests.Response:
        '''Выполняет DELETE-запрос.

        Args:
            url: URL запроса.
            *args: Позиционные аргументы для requests.delete.
            **kwargs: Именованные аргументы для requests.delete.

        Returns:
            requests.Response: Ответ сервера на DELETE-запрос.'''
        return requests.delete(auth=self.auth, url=self.base_url + url, *args, **kwargs)


@lru_cache(maxsize=None)
def get_client(auth: bool = False, *args, **kwargs) -> Client:
    '''Создаёт экземпляр клиента API.
    Может отдавать как авторизованный, так и неавторизованный клиент, в зависимости от флага auth

    Args:
        auth: Флаг аутентификации (по умолчанию False).
        *args: Позиционные аргументы для Client.
        **kwargs: Именованные аргументы для Client.

    Returns:
        Client: Экземпляр клиента API.'''

    if not auth:
        return Client(*args, **kwargs)

    # берём авторизацию из базовых настроек
    auth = base_settings.user

    return Client(auth=auth, *args, **kwargs)
