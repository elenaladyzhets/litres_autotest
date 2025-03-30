import allure
from data.book import Book
from model.pages.cart_page import cart_page
from model.pages.book_page import book_page


@allure.epic('Добавление книги в корзину')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Проверка добавления книги в корзину')
@allure.tag('web')
@allure.severity('normal')
def test_add_book_to_cart():
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
    cart_page.book_should_be_in_cart(book)