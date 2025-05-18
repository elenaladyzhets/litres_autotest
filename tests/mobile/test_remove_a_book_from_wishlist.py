import allure
from model.pages.mobile.main_page import main_page
from model.pages.mobile.search_page import search_page
from model.pages.mobile.book_page import book_page


@allure.epic('MOBILE. Remove book from wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Remove book from wishlist"')
@allure.tag('mobile')
@allure.severity('normal')

def test_remove_book_from_wishlist(android_management):
     main_page.selecting_application_language()
     main_page.notification()

     search_page.searching_book()
     search_page.book_must_be_found()
     search_page.choosing_book()

     book_page.add_book_to_wishlist()
     book_page.go_to_wishlist_tab()
     book_page.book_must_be_added_to_wishlist()
     book_page.remove_book_from_wishlist()
     book_page.go_to_wishlist_tab()
     book_page.book_must_be_removed_from_wishlist()
