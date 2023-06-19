from typing import Optional, TypedDict

from pydantic import BaseModel, Field

from utils.fakers import (
    random_list_of_strings, random_string, random_float,
    invalid_string, invalid_float, too_long_string)


class Character(BaseModel):
    '''Модель данных для представления персонажа.'''
    education: Optional[str] = Field(default_factory=random_string, title='Education')
    height: Optional[float] = Field(default_factory=random_float, title='Height')
    identity: Optional[str] = Field(default_factory=random_string, title='Identity')
    name: str = Field(default_factory=random_string, title='Name')
    other_aliases: Optional[str] = Field(default_factory=random_list_of_strings, title='Other Aliases')
    universe: Optional[str] = Field(default_factory=random_string, title='Universe')
    weight: Optional[float] = Field(default_factory=random_float, title='Weight')


class CharactersList(BaseModel):
    '''Модель данных для представления списка персонажей.'''
    __root__: list[Character]


class CharacterDict(TypedDict):
    '''Тип данных для представления персонажа в виде словаря.'''
    education: str
    height: float
    identity: str
    name: str
    other_aliases: str
    universe: str
    weight: float


class CharacterNoRequiredField(BaseModel):
    '''Модель данных для представления персонажа без обязательных полей.
    Для тестирования негативных сценариев'''
    education: Optional[str] = Field(default_factory=random_string, title='Education')
    height: Optional[float] = Field(default_factory=random_float, title='Height')
    identity: Optional[str] = Field(default_factory=random_string, title='Identity')
    other_aliases: Optional[str] = Field(default_factory=random_list_of_strings, title='Other Aliases')
    universe: Optional[str] = Field(default_factory=random_string, title='Universe')
    weight: Optional[float] = Field(default_factory=random_float, title='Weight')


# и невалидный словарик, каждый раз он будет разным
# и будет проверять разные типы невалидных данных, за счёт того, что функции
# invalid_* возвращают случайное значение из списка невалидных
# можно, конечно, каждый раз проверять всё, через pytest.mark.parametrize,
# но это кажется излишним
CharacterDictInvalid = {
        'education': invalid_string(),
        'height': invalid_float(),
        'identity': invalid_string(),
        'name': invalid_string(),
        'other_aliases': invalid_string(),
        'universe': invalid_string(),
        'weight': invalid_float(),
    }

# ограничения на максимальное значение float я не нашла
CharacterDictTooLong = {
        'education': too_long_string(),
        'identity': invalid_string(),
        'name': invalid_string(),
        'other_aliases': invalid_string(),
        'universe': invalid_string(),
    }
