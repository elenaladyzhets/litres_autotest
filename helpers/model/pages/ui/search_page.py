from selene import browser, have
import allure

from config import config


class SearchPage:
    def open(self):
        with allure.step('Open main page'):
            browser.open(config.base_ui_url)
            return self

    def search_book_by_title(self, book):
        with allure.step('Search book wia button'):
            browser.element('[data-testid="search__input"]').type(book.name)
            browser.element('[data-testid="search__button"]').click()
            return self

    def search_book_by_title_enter(self, book):
        with allure.step('Search book via Enter'):
            browser.element('[data-testid="search__input"]').type(book.name)
            browser.element('[data-testid="search__input"]').press_enter()
            return self

    def find_with_title(self, book):
        with allure.step('Check valid search result'):
            browser.all('[data-testid=art__title]').first.should(have.text(book.name))
            return self

    def find_empty_result(self):
        with allure.step('Check unvalid search result'):
            browser.element('[data-testid=search-title__wrapper]').should(have.text('ничего не найдено'))
            return self



search_page = SearchPage()