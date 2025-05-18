import allure
from utils.api_requests import api_delete


@allure.tag('API. Remove book')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Remove book from the wishlist')
@allure.tag('api')
@allure.severity('normal')

def test_delete_book_from_wishlist():
    url = '/wishlist/arts/'
    id_book = '11132511'

    with allure.step('Remove book from the wishlist'):
        result = api_delete(url + id_book)

    assert result.status_code == 204
    assert result.text == ''