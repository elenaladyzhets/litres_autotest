import allure
from data.book import Book
from model.pages.ui.cart_page import cart_page
from model.pages.ui.book_page import book_page


@allure.epic('UI. Removing a book to the trash')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Check if a book has been removed from the trash')
@allure.tag('ui')
@allure.severity('normal')
def test_add_book_to_basket():
    book = Book(
        name='Кладбище домашних животных',
        author='Стивен Кинг',
        url='stiven-king/kladbische-domashnih-zhivotnyh-42225823/',
        price='499 ₽'
    )
    book_page.open(book)
    book_page.adding_book_to_cart()
    book_page.close_message_window()
    cart_page.open_cart()
    cart_page.remove_book_from_cart()
    cart_page.cart_should_be_empty()