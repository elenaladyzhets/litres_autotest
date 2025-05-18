import allure
from model.pages.mobile.main_page import main_page
from model.pages.mobile.search_page import search_page
from model.pages.mobile.book_page import book_page


@allure.epic('MOBILE. Add book to wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Add book to wishlist"')
@allure.tag('mobile')
@allure.severity('normal')

def test_add_book_to_wishlist(android_management):
     main_page.selecting_application_language()
     main_page.notification()

     search_page.searching_book()
     search_page.book_must_be_found()
     search_page.choosing_book()

     book_page.add_book_to_wishlist()
     book_page.go_to_wishlist_tab()
     book_page.book_must_be_added_to_wishlist()


