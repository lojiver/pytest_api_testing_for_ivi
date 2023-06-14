import pytest
from dotenv import dotenv_values
import requests


@pytest.fixture
def auth():
    env = dotenv_values('.env')
    login = env['LOGIN']
    password = env['PASSWORD']
    return (login, password)


@pytest.fixture
def headers():
    return {'Content-type': 'application/json'}


@pytest.fixture
def reset_base(auth, url_reset):
    requests.post(url_reset, auth=auth)


@pytest.fixture
def required_keys():
    required_keys = {
        "name",
        "other_aliases",
    }
    return required_keys


@pytest.fixture
def expected_keys():
    expected_keys = {
        "education",
        "height",
        "identity",
        "name",
        "other_aliases",
        "universe",
        "weight"
    }
    return expected_keys


@pytest.fixture
def url_multi():
    env = dotenv_values('.env')
    api = env['API']
    return api + 'characters'


@pytest.fixture
def url_one_id():
    env = dotenv_values('.env')
    api = env['API']
    return api + 'character'


@pytest.fixture
def url_reset():
    env = dotenv_values('.env')
    api = env['API']
    return api + 'reset'
