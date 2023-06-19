import pytest

from http import HTTPStatus
from pydantic.schema import schema

from base.api.character_api import (
    create_character_api, delete_character_api,
    get_character_api, get_characters_api, update_character_api)
from utils.assertions.character import assert_character
from utils.assertions.solutions import assert_status_code, validate_schema, validate_error_text
from utils.fakers import random_string
from utils.models.character import (
    Character, CharacterDict, CharactersList,
    CharacterNoRequiredField, CharacterDictInvalid,
    CharacterDictTooLong)
from utils.constants import Errors


@pytest.mark.characters
class TestCharactersAuthorizedValid:
    '''Класс с тестами для авторизованного доступа к операциям с персонажами (валидные сценарии).'''
    def test_get_characters(self):
        '''Тест получения списка персонажей.
        Проверяет, что получен корректный статус-код, схема списка персонажей валидна.'''
        response = get_characters_api(auth=True)
        json_response: list[CharacterDict] = response.json()['result']

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, schema([CharactersList]))

    def test_create_character(self):
        '''Тест создания персонажа.
        Проверяет, что получен корректный статус-код, созданный персонаж совпадает с отправленным,
        схема созданного персонажа валидна.'''
        payload = Character()

        response = create_character_api(payload.dict(), auth=True)
        json_response: CharacterDict = response.json()['result']

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_character(
            expected_character=payload,
            actual_character=json_response
        )

        validate_schema(json_response, Character.schema())

    def test_get_character(self, function_character: Character):
        '''Тест получения конкретного персонажа.
        Проверяет, что получен корректный статус-код, полученный персонаж совпадает с отправленным,
        схема полученного персонажа валидна.'''
        response = get_character_api(function_character.name, auth=True)
        json_response: CharacterDict = response.json()['result']

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_character(
            expected_character=function_character,
            actual_character=json_response
        )

        validate_schema(json_response, Character.schema())

    def test_update_character(self, function_character: Character):
        '''Тест обновления персонажа.
        Проверяет, что получен корректный статус-код, обновленный персонаж совпадает с отправленным,
        схема обновленного персонажа валидна.'''
        payload = Character()
        payload.name = function_character.name
        response = update_character_api(payload.dict(), auth=True)
        json_response: CharacterDict = response.json()['result']

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_character(
            expected_character=payload,
            actual_character=json_response
        )

        validate_schema(json_response, Character.schema())

    def test_delete_character(self, function_character: Character):
        '''Тест удаления персонажа.
        Проверяет, что получен корректный статус-код при удалении, персонаж больше не найден в системе.'''
        delete_character_response = delete_character_api(function_character.name, auth=True,)
        get_character_response = get_character_api(function_character.name, auth=True)

        assert_status_code(delete_character_response.status_code, HTTPStatus.OK)
        assert_status_code(
            get_character_response.status_code, HTTPStatus.NOT_FOUND
        )


@pytest.mark.characters
@pytest.mark.parametrize('get_list', [get_characters_api])
@pytest.mark.parametrize('with_payload', [create_character_api, update_character_api])
@pytest.mark.parametrize('with_name', [get_character_api, delete_character_api])
def test_character_unauthorized(function_character: Character, get_list: callable,
                                with_name: callable, with_payload: callable):
    '''Тесты операций с персонажами без авторизации.
    Проверяют, что получен корректный статус код UNAUTHORIZED для каждой операции.'''

    # разделила запросы на группы по аргументам, скорее всего можно ещё компактнее сделать,
    # но я не придумаю и не видела готовых решений
    response = get_list()
    assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)

    payload = Character()
    response = with_payload(payload.dict())
    assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)

    response = with_name(function_character.name)
    assert_status_code(response.status_code, HTTPStatus.UNAUTHORIZED)


@pytest.mark.characters
class TestCharactersAuthorizedInvalid:
    '''Класс с тестами для авторизованного доступа к операциям с персонажами (невалидные сценарии).'''
    def test_create_character_no_name(self):
        '''Тест создания персонажа без обязательных параметров.
        Имя - единственный обязательный параметр, поэтому только без него
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        payload = CharacterNoRequiredField()

        response = create_character_api(payload.dict(), auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

        validate_error_text(expected_error=Errors.NO_REQUIRED_FIELD, response_text=text_response)

    def test_create_character_invalid_data(self):
        '''Тест создания персонажа с невалидными данными.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        payload = CharacterDictInvalid

        response = create_character_api(payload, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

        validate_error_text(expected_error=Errors.NOT_VALID_VALUE, response_text=text_response)

    def test_create_character_too_long_string(self):
        '''Тест создания персонажа с слишком длинными значениями строк.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        payload = CharacterDictTooLong

        response = create_character_api(payload, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

        validate_error_text(expected_error=Errors.TOO_LONG, response_text=text_response)

    def test_create_character_already_exists_name(self, function_character):
        '''Тест создания персонажа с уже существующим именем.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        payload = Character()
        payload.name = function_character.name
        response = create_character_api(payload.dict(), auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        validate_error_text(expected_error=Errors.ALREADY_EXISTS, response_text=text_response)

    def test_create_character_in_full_base(self, fill_base_to_full):
        '''Тест создания персонажа при полной заполненности базы данных.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        fill_base_to_full
        payload = Character()

        response = create_character_api(payload.dict(), auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        validate_error_text(expected_error=Errors.FULL_BASE, response_text=text_response)

    def test_get_name_not_exists(self):
        '''Тест получения несуществующего персонажа.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        response = get_character_api(random_string, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        validate_error_text(expected_error=Errors.NO_SUCH_NAME, response_text=text_response)

    def test_get_name_in_other_aliases(self, function_character: Character):
        '''Тест получения персонажа по имени, которое является псевдонимом другого персонажа.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        response = get_character_api(function_character.other_aliases, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        validate_error_text(expected_error=Errors.NO_SUCH_NAME, response_text=text_response)

    def test_update_character_no_name(self):
        '''Тест обновления персонажа без обязательных параметров.
        Имя - единственный обязательный параметр, поэтому только без него
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        payload = CharacterNoRequiredField()

        response = update_character_api(payload.dict(), auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

        validate_error_text(expected_error=Errors.NO_REQUIRED_FIELD, response_text=text_response)

    def test_update_character_invalid_data(self, function_character):
        '''Тест обновления персонажа с невалидными данными.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        payload = CharacterDictInvalid
        payload['name'] = function_character.name
        response = update_character_api(payload, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

        validate_error_text(expected_error=Errors.NOT_VALID_VALUE, response_text=text_response)

    def test_delete_name_not_exists(self):
        '''Тест удаления несуществующего персонажа.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''

        response = delete_character_api(random_string, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        validate_error_text(expected_error=Errors.NO_SUCH_NAME, response_text=text_response)

    def test_delete_name_in_other_aliases(self, function_character: Character):
        '''Тест удаления персонажа с именем, являющимся псевдонимом другого персонажа.
        Проверяет, что получен корректный статус код BAD_REQUEST и сообщение об ошибке соответствует ожидаемому.'''
        response = delete_character_api(function_character.other_aliases, auth=True)
        text_response = response.text

        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
        validate_error_text(expected_error=Errors.NO_SUCH_NAME, response_text=text_response)
