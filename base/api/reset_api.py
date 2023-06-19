from requests import Response

from base.client import get_client
from utils.constants import APIRoutes


def post_reset_api(auth: bool = False) -> Response:
    '''Выполняет POST-запрос для сброса данных.

    Args:
        auth (bool, optional): Флаг аутентификации. По умолчанию False.

    Returns:
        Response: Ответ сервера.'''
    client = get_client(auth=auth)
    return client.post(url=APIRoutes.RESET)
