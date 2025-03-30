import allure
from data.book import Book
from model.pages.wishlist_page import wishlist_page
from model.pages.book_page import book_page
from model.pages.cart_page import cart_page


@allure.epic('Добавление в отложенное')
@allure.label('owner', 'Elena Ladyzhets')
@allure.feature('Добавление в отложенное через страницу книги')
@allure.tag('web')
@allure.severity('normal')

def test_add_book_to_wishlist_from_book_page():
    book = Book(
        name='Сияние',
        author='Стивен Кинг',
        url='stiven-king/siyanie-48428036/',
        price=''
    )

    book_page.open(book)
    book_page.adding_book_to_favorites()
    wishlist_page.open_wishlist()
    wishlist_page.book_must_be_added_to_favorites(book)

#@allure.epic('Добавление в отложенное')
#@allure.label('owner', 'Elena Ladyzhets')
#@allure.feature('Добавление в отложенное через корзину')
#@allure.tag('web')
#@allure.severity('normal')

#def test_add_book_to_wishlist_from_cart():
 #   book = Book(
  #      name='Кладбище домашних животных',
   #     author='Стивен Кинг',
    #    url='stiven-king/kladbische-domashnih-zhivotnyh-42225823/',
     #   price='499 ₽'
    #)

   # book_page.open(book)
   # book_page.adding_book_to_favorites()
   # wishlist_page.open_wishlist()
   # wishlist_page.book_must_be_added_to_favorites(book)
