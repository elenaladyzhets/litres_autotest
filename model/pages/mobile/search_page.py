from selene import browser, have, be
import allure
from appium.webdriver.common.appiumby import AppiumBy


class SearchPage:
    def search_book(self):
        with allure.step('Search valid book'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).should(be.visible).click()
            browser.element((AppiumBy.ID, 'ru.litres.android:id/et_search_query')).type('The Green Mile')
            browser.element((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText')).click()
        return self

    def book_should_be_found(self):
        with allure.step('Check book is found'):
            browser.element((AppiumBy.XPATH,'(//android.widget.TextView[@resource-id="ru.litres.android:id/textViewBookName"])[1]')).should(have.text('Зеленая миля / The Green Mile'))
        return self

    def search_non_valid_book(self):
        with allure.step('Search unvalid book'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/search")).click()
            browser.element((AppiumBy.ID, "ru.litres.android:id/et_search_query")).type('4353tgr8y7557g')
            browser.element((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText')).click()
        return self

    def book_should_not_be_found(self):
        with allure.step('Check book is not found'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/title")).should(have.text('Nothing found'))
            (browser.element((AppiumBy.ID, "ru.litres.android:id/tv_books_search_empty_message")).should(have.text('Make sure you entered the search query correctly')))
        return self

    def choose_book(self):
        with allure.step('Choose a book'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/textViewBookName")).click()
        return self



search_page = SearchPage()