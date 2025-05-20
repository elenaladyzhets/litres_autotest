import allure
from data.book import Book
from model.pages.ui.search_page import search_page


@allure.epic('UI. Search a book')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Check the book search on the main page via the button')
@allure.tag('ui')
@allure.severity('normal')

def test_search_valid_book_button():
    book = Book(
        name='Зелёная миля',
        author='Стивен Кинг',
        url='',
        price=''
    )

    search_page.open()
    search_page.search_book_by_title(book)
    search_page.find_with_title(book)

@allure.epic('UI. Search a book')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Check the book search on the main page via "Enter"')
@allure.tag('ui')
@allure.severity('normal')

def test_search_valid_book_enter():
    book = Book(
        name='Зелёная миля',
        author='Стивен Кинг',
        url='',
        price=''
    )

    search_page.open()
    search_page.search_book_by_title_enter(book)
    search_page.find_with_title(book)


@allure.epic('UI. Search a book')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Check for a non-existent book search')
@allure.tag('ui')
@allure.severity('normal')
def test_search_non_valid_book():
    book = Book(
        name='123135арапн5674ирва',
        author='25пвав56880рпрке6',
        url='',
        price=''
    )
    search_page.open()
    search_page.search_book_by_title(book)
    search_page.find_empty_result()