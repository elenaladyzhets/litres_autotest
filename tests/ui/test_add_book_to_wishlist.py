import allure
from helpers.data import Book
from helpers.model.pages.ui import wishlist_page
from helpers.model.pages.ui.book_page import book_page
from helpers.model.pages.ui import cart_page
import time


@allure.epic('UI. Add to wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Add to wishlist via book page')
@allure.tag('ui')
@allure.severity('normal')

def test_add_book_to_wishlist_from_book_page():
    book = Book(
        name='Сияние',
        author='Стивен Кинг',
        url='stiven-king/siyanie-48428036/',
        price=''
    )

    book_page.open(book)
    book_page.add_book_to_wishlist()
    wishlist_page.open_wishlist()
    wishlist_page.book_should_be_in_wishlist(book)

@allure.epic('UI. Add to wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Add to wishlist via cart')
@allure.tag('ui')
@allure.severity('normal')

def test_add_book_to_wishlist_from_cart():
    book = Book(
        name='Кладбище домашних животных',
        author='Стивен Кинг',
        url='stiven-king/kladbische-domashnih-zhivotnyh-42225823/',
        price='499 ₽'
    )

    book_page.open(book)
    book_page.add_book_to_cart()
    book_page.close_message_window()
    cart_page.open_cart()

    time.sleep(2)

    cart_page.add_book_to_wishlist_from_cart()
    wishlist_page.open_wishlist()
    wishlist_page.book_should_be_in_wishlist(book)
