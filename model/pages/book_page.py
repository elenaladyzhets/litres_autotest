from selene import browser, be, have, command
import allure


class BookPage:
    def open(self, book):
        with allure.step('Открытие страницы книги'):
           browser.open(f"book/{book.url}")
           return self

    def adding_book_to_cart(self):
        with allure.step('Добавление книги в корзину'):
           browser.driver.refresh()
           if browser.element('[data-testid=book__addToCartButton]').with_(timeout=7).matching(be.present):
               browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
           else:
               browser.element('[data-testid=book-sale-block__PPD--wrapper]').should(be.clickable).click()
               browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
           return self

    def adding_book_to_favorites(self):
        with allure.step('Добавление книги в избранное из страницы книги'):
            browser.element('[data-testid="wishlist__button"]').should(be.visible).click()
            return self

    def close_message_window(self):
        with allure.step('Закрытие модального окна'):
            browser.all('#modal').with_(timeout=5).wait_until(
                have.size_greater_than_or_equal(1)
            )
            browser.all('#modal').perform(command.js.remove)
            return self


book_page = BookPage()