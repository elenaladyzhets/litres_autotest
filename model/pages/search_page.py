from selene import browser, have
import allure


class SearchPage:
    def open(self):
        with allure.step('Открытие главной страницы'):
            browser.open('https://www.litres.ru/')
            return self

    def search_book_by_title(self, book):
        with allure.step('Поиск книги через кнопку'):
            browser.element('[data-testid="search__input"]').type(book.name)
            browser.element('[data-testid="search__button"]').click()
            return self

    def search_book_by_title_enter(self, book):
        with allure.step('Поиск книги через Enter'):
            browser.element('[data-testid="search__input"]').type(book.name)
            browser.element('[data-testid="search__input"]').press_enter()
            return self

    def find_with_title(self, book):
        with allure.step('Проверка результатов валидного поиска'):
            browser.all('[data-testid=art__title]').first.should(have.text(book.name))
            return self

    def find_empty_result(self):
        with allure.step('Проверка результатов невалидного поиска'):
            browser.element('[data-testid=search-title__wrapper]').should(have.text('ничего не найдено'))
            return self



search_page = SearchPage()