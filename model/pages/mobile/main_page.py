from selene import browser, be
import allure
from appium.webdriver.common.appiumby import AppiumBy


class AndroidMainPage:
    @staticmethod
    def selecting_application_language():
        with allure.step('Selecting application language'):
           browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENGLISH")')).click()
           browser.element((AppiumBy.ID, "ru.litres.android:id/choosebutton")).click()


    @staticmethod
    def notification():
        with allure.step('Notification'):
           browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")).wait_until(be.visible)
           browser.element((AppiumBy.ID,"com.android.permissioncontroller:id/permission_deny_button",)).click()


main_page = AndroidMainPage()