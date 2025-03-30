import allure
from data.book import Book
from model.pages.search_page import search_page


@allure.epic('Поиск')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Проверка поиска книги на главной странице через кнопку')
@allure.tag('web')
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

@allure.epic('Поиск')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Проверка поиска книги на главной странице через enter')
@allure.tag('web')
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


@allure.epic('Поиск')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Проверка поиска несуществующей книги')
@allure.tag('web')
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