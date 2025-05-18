import allure
from utils.api_requests import api_put_to_wishlist


@allure.tag("API. Add book")
@allure.label("owner", "Elena Ladyzhets")
@allure.feature("Add book to wishlist")
@allure.tag('api')
@allure.severity('normal')
def test_add_book_to_wishlist():
    url = '/wishlist/arts/'
    id_book = '11132511'

    with allure.step('Add book to the wishlist'):
        result = api_put_to_wishlist(url + id_book)

    assert result.status_code == 204
    assert result.text == ''