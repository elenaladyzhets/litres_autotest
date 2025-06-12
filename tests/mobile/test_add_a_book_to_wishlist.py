import allure
from helpers.model.pages.mobile.main_page import main_page
from helpers.model.pages.mobile import search_page
from helpers.model.pages.mobile.book_page import book_page


@allure.epic('MOBILE. Add book to wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Add book to wishlist"')
@allure.tag('mobile')
@allure.severity('normal')

def test_add_book_to_wishlist(android_management):
     main_page.select_application_language()
     main_page.notification()

     search_page.search_book()
     search_page.book_should_be_found()
     search_page.choose_book()

     book_page.add_book_to_wishlist()
     book_page.open_wishlist()
     book_page.book_should_be_in_wishlist()


