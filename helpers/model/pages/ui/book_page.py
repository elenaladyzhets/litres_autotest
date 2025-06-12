from selene import browser, be, have, command
import allure

from config import config


class BookPage:
    def open(self, book):
        with allure.step('Open book page'):
           browser.open(f"{config.base_ui_url}/{book.url}")
           return self

    def add_book_to_cart(self):
        with allure.step('Add book to cart'):
           browser.driver.refresh()
           if browser.element('[data-testid=book__addToCartButton]').with_(timeout=7).matching(be.present):
               browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
           else:
               browser.element('[data-testid=book-sale-block__PPD--wrapper]').should(be.clickable).click()
               browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
           return self

    def add_book_to_wishlist(self):
        with allure.step('Add book to wishlist from book page'):
            browser.all('[data-testid="wishlist__button"]').element_by(be.visible).click()
            return self

    def close_message_window(self):
        with allure.step('Close modal window'):
            browser.all('#modal').with_(timeout=5).wait_until(
                have.size_greater_than_or_equal(1)
            )
            browser.all('#modal').perform(command.js.remove)
            return self


book_page = BookPage()