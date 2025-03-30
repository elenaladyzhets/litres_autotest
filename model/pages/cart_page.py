from selene import browser, have, be
import allure


class CartPage:

    def open_cart(self):
        with allure.step('Открытие корзины'):
            browser.element('[data-testid=tab-basket]').click()
            return self

    def book_should_be_in_cart(self, book):
        with allure.step('Проверка книги в корзине'):
            browser.element('[data-testid=cart__bookCardTitle--wrapper]').should(have.text(book.name))
            browser.element('[data-testid=cart__bookCardAuthor--wrapper]').should(have.text(book.author))
            browser.element('[data-testid=cart__bookCardDiscount--wrapper]').should(have.text(str(book.price)))
            return self

    def adding_book_to_favorites_from_cart(self):
        with allure.step('Добавление книги в избранное из корзины'):
           browser.element('.FunctionalButton_funcButtonContent__ns82k').should(be.visible).click()
           return self

    def removing_book_from_favorites_from_cart(self):
        with allure.step('Удаление книги из избранного из корзины'):
           browser.open("my-books/cart/")
           browser.element('.FunctionalButton_funcButtonContent__ns82k').should(be.visible).click()
           return self

    def remove_book_from_cart(self):
        with allure.step('Удаление книги из корзины'):
            browser.all('[data-testid=cart__listDeleteButton]').first.click()
            browser.all('[data-testid=button__content]').element_by(have.text('Удалить')).click()
            return self

    def cart_should_be_empty(self):
        with allure.step('Проверка, что корзина пустая'):
            browser.element('[data-testid=cart__emptyState--wrapper]').should(have.text('Корзина пуста'))
            return self

cart_page = CartPage()