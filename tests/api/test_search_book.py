import allure
import jsonschema
from model.schemas.load_schema import load_schema
from utils.api_requests import api_get


@allure.epic('API. Search a book')
@allure.label("owner", "Elena Ladyzhets")
@allure.feature("Search valid book")
@allure.tag('api')
@allure.severity('normal')
def test_successful_searching_of_book_by_title():
    schema = load_schema('successfully_search_book.json')

    book_title = 'Мальчик в полосатой пижаме'
    full_name='Джон Бойн'
    types = 'text_book'
    url = f'/search'
    params = {"q": book_title, "types": types, 'full_name': full_name}
    result = api_get(url, params=params)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['payload']['data'][0]['type'] == "text_book"


@allure.epic('API. Search a book')
@allure.label("owner", "Elena Ladyzhets")
@allure.feature("Search unvalid book")
@allure.tag('api')
@allure.severity('normal')
def test_unsuccessful_searching_of_book_by_title():
    schema = load_schema('unsuccessfully_search_book.json')

    book_title = '436ерреар5756рап'
    types = 'text_book'
    url = f'/search'
    params = {"q": book_title, "types": types}
    result = api_get(url, params=params)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['payload']['data']) == 0
