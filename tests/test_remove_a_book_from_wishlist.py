import allure
from data.book import Book
from model.pages.wishlist_page import wishlist_page
from model.pages.book_page import book_page
from model.pages.cart_page import cart_page


@allure.epic('Удаление из отложенного')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Удаление из отложенного через страницу "Отложенные"')
@allure.tag('web')
@allure.severity('normal')

def test_remove_book_to_wishlist_from_wishlist_page():
    book = Book(
        name='Сияние',
        author='Стивен Кинг',
        url='stiven-king/siyanie-48428036/',
        price=''
    )

    book_page.open(book)
    book_page.adding_book_to_favorites()
    wishlist_page.open_wishlist()
    wishlist_page.removing_book_from_favorites()
    wishlist_page.book_must_be_removed_from_favorites()


@allure.epic('Удаление из отложенного')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Удаление из отложенного через корзину"')
@allure.tag('web')
@allure.severity('normal')

def test_remove_book_to_wishlist_from_cart_page():
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
    cart_page.adding_book_to_favorites_from_cart()
    cart_page.removing_book_from_favorites_from_cart()
    wishlist_page.open_wishlist()
    wishlist_page.book_must_be_removed_from_favorites()
