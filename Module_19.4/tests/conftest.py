import pytest
import requests
import json

base_url = "https://petfriends.skillfactory.ru/"

@pytest.fixture()
def get_api_key() -> json:
    """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
    JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""
    print("Фикстура начало")

    headers = {
        'email': "shevsyi@yandex.ru",
        'password': '061786&pkm_pchZH',
    }
    res = requests.get(base_url + 'api/key', headers=headers)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print("фикстура конец")
    return status, result

@pytest.fixture(autouse=True)
def say_hello():
    print("Test начало")

@pytest.fixture(autouse=True)
def say_godbay():
    print('готовимся к прощанию')
    yield
    print("Tests конец")
