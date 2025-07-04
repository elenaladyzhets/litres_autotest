import allure
from helpers.data import Book
from helpers.model.pages.ui import cart_page
from helpers.model.pages.ui.book_page import book_page


@allure.epic('UI. Remove a book to the trash')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Remove book from cart')
@allure.tag('ui')
@allure.severity('normal')
def test_remove_book_from_cart():
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
    cart_page.remove_book_from_cart()
    cart_page.cart_should_be_empty()