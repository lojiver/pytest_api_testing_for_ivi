# Проект тестирования api для ivi


## Описание проекта
Тестирует обращения к API http://rest.test.ivi.ru/v2/ с тремя эндпоинтами:
 - /character
 - /characters
 - /reset

Авторизацию необходимо передавать в каждом запросе в формате
```curl 'http://rest.test.ivi.ru/v2/characters' -u username:password```

Сценарии тестирования содержатся в xls-файле в корне проекта.

P.S. У меня в настройках VSCode указано ```python.linting.flake8Args": ["--max-line-length=120"]```, поэтому код не соответствует стандартному ограничению PEP8 на длину строки.

## Использованные технологии
- jsonschema==4.17.3
- pydantic==1.10.9
- pytest==7.3.2
- python-dotenv==1.0.0
- requests==2.31.0

## Инструкции по запуску
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd pytest_api_testing_for_ivi/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить pytest:
```
pytest
```

Два теста проверки статус-кода возвращают failed, потому что API возвращает несоответствующий ситуации статус-код.

## Требования к версии Python
Работает на Python 3.11.0
