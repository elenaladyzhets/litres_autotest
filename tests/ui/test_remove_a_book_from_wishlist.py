import allure
from data.book import Book
from model.pages.ui.wishlist_page import wishlist_page
from model.pages.ui.book_page import book_page
from model.pages.ui.cart_page import cart_page
import time


@allure.epic('UI. Remove from wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Remove from wishlist via the "Wishlist" page')
@allure.tag('ui')
@allure.severity('normal')

def test_remove_book_to_wishlist_from_wishlist_page():
    book = Book(
        name='Сияние',
        author='Стивен Кинг',
        url='stiven-king/siyanie-48428036/',
        price=''
    )

    book_page.open(book)
    book_page.add_book_to_wishlist()
    wishlist_page.open_wishlist()
    wishlist_page.remove_book_from_wishlist()
    wishlist_page.book_should_not_be_in_wishlist()


@allure.epic('UI. Remove from wishlist')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Remove from wishlist via cart')
@allure.tag('ui')
@allure.severity('normal')

def test_remove_book_to_wishlist_from_cart_page():
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
    cart_page.add_book_to_wishlist_from_cart()
    cart_page.remove_book_from_wishlist_from_cart()
    wishlist_page.open_wishlist()
    wishlist_page.book_should_not_be_in_wishlist()
