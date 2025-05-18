from selene import browser, be, have
import allure
from appium.webdriver.common.appiumby import AppiumBy


class BookPage:
    def add_book_to_wishlist(self):
        with allure.step('Add a book to wishlist'):
            browser.element((AppiumBy.ID,'ru.litres.android:id/imageViewBookCardFavourite')).click()
        return self

    def go_to_wishlist_tab(self):
        with allure.step('Go to the wishlist tab'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'My books')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Favorites")')).click()
        return self

    def book_must_be_added_to_wishlist(self):
        with allure.step('Checking that the selected book has been added to wishlist'):
            (browser.element((AppiumBy.ID, "ru.litres.android:id/textViewBookName")).should(have.text("Зеленая миля / The Green Mile")))
        return self

    def remove_book_from_wishlist(self):
        with allure.step('Removing a book from wishlist'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/textViewBookName")).click()
            browser.element((AppiumBy.ID, "ru.litres.android:id/imageViewBookCardFavourite")).click()
        return self

    def book_must_be_removed_from_wishlist(self):
        with allure.step('Checking that the selected book has been removed from wishlist'):
            browser.element((AppiumBy.ID, "ru.litres.android:id/textViewDescriptionEmptySection")).should(have.text('Everything you save for later will be here.'))
        return self


book_page = BookPage()