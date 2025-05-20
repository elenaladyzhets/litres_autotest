import allure
from model.pages.mobile.main_page import main_page
from model.pages.mobile.search_page import search_page


@allure.epic('MOBILE. Search a book')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Search valid book search on mobile app"')
@allure.tag('mobile')
@allure.severity('normal')

def test_search_valid_book(android_management):
     main_page.select_application_language()
     main_page.notification()

     search_page.search_book()
     search_page.book_should_be_found()


@allure.epic('MOBILE. Search a book')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Search non valid book search on mobile app"')
@allure.tag('mobile')
@allure.severity('normal')

def test_search_non_valid_book( android_management):
     main_page.select_application_language()
     main_page.notification()

     search_page.search_non_valid_book()
     search_page.book_should_not_be_found()


