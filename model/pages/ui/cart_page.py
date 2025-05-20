from selene import browser, have, be
import allure


class CartPage:

    def open_cart(self):
        with allure.step('Open cart'):
            browser.element('[data-testid=tab-basket]').click()
            return self

    def book_should_be_in_cart(self, book):
        with allure.step('Check book in cart'):
            browser.element('[data-testid=cart__bookCardTitle--wrapper]').should(have.text(book.name))
            browser.element('[data-testid=cart__bookCardAuthor--wrapper]').should(have.text(book.author))
            browser.element('[data-testid=cart__bookCardDiscount--wrapper]').should(have.text(str(book.price)))
            return self

    def add_book_to_wishlist_from_cart(self):
        with allure.step('Add book to wishlist from cart'):
           browser.all('.FunctionalButton_funcButtonContent__ns82k').element_by(be.visible).click()
           return self

    def remove_book_from_wishlist_from_cart(self):
        with allure.step('Remove book from wishlist from cart'):
           browser.all('.FunctionalButton_funcButtonContent__ns82k').element_by(be.visible).click()
           return self

    def remove_book_from_cart(self):
        with allure.step('Remove book from cart'):
            browser.all('[data-testid=cart__listDeleteButton]').first.click()
            browser.all('[data-testid=button__content]').element_by(have.text('Удалить')).click()
            return self

    def cart_should_be_empty(self):
        with allure.step('Check empty cart'):
            browser.element('[data-testid=cart__emptyState--wrapper]').should(have.text('Корзина пуста'))
            return self

cart_page = CartPage()