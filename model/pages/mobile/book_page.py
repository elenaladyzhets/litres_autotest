from selene import browser, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


class BookPage:
    def add_book_to_wishlist(self):
        with allure.step('Add a book to wishlist'):
            browser.element((AppiumBy.ID,'ru.litres.android:id/imageViewBookCardFavourite')).click()
        return self

    def open_wishlist(self):
        with allure.step('Open wishlist page'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'My books')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Favorites")')).click()
        return self

    def book_should_be_in_wishlist(self):
        with allure.step('Check book in wishlist'):
            (browser.element((AppiumBy.ID, "ru.litres.android:id/textViewBookName")).should(have.text("Зеленая миля / The Green Mile")))
        return self

    def remove_book_from_wishlist(self):
        with allure.step('Remove book from wishlist'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/textViewBookName")).click()
            browser.element((AppiumBy.ID, "ru.litres.android:id/imageViewBookCardFavourite")).click()
        return self

    def book_should_be_removed_from_wishlist(self):
        with allure.step('Check empty wishlist'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/textViewDescriptionEmptySection")).should(have.text('Everything you save for later will be here.'))
        return self


book_page = BookPage()