import allure
import jsonschema

from helpers.model.schemas.load_schema import load_schema
from helpers.utils.api_requests import api_put


@allure.epic('API. Add book to cart')
@allure.label("owner", "Elena Ladyzhets")
@allure.feature("Add book to cart")
@allure.tag('api')
@allure.severity('normal')

def test_adding_book_to_cart():
    schema = load_schema('successful_adding_book_to_cart.json')

    url = "/cart/arts/add"
    id_book = [11132511]
    headers = {"Content-Type": "application/json"}

    result = api_put(url, headers=headers, json={"art_ids": id_book})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['payload']['data']['added_art_ids'] == id_book
    assert result.json()['payload']['data']['failed_art_ids'] == []