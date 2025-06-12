import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
from config import config
from helpers.utils import  tools
from appium import webdriver

from helpers.utils.attach import add_mobile_screenshot, add_mobile_xml, add_mobile_bstack_video


@pytest.fixture(scope='function')
def android_management():
    try:
        options_dict = {
            'app': config.app if config.app.startswith('bs://')
            else tools.path_to_apk(config.app),
            'appPackage': 'ru.litres.android',
            'appActivity': 'ru.litres.android.splash.MainSplashAlias',
            'appWaitActivity': 'ru.litres.android.splash.*'
        }

        if config.udid:
            options_dict['udid'] = config.udid
        if config.deviceName:
            options_dict['deviceName'] = config.deviceName
        if config.platformVersion:
            options_dict['platformVersion'] = config.platformVersion

        options = UiAutomator2Options().load_capabilities(options_dict)

        if config.context == 'bstack':
            if not config.bstack_userName or not config.bstack_accessKey:
                raise ValueError("BrowserStack credentials not found")

            allure.attach(
                f"BrowserStack User: {config.bstack_userName}\n"
                f"App: {config.app}\n"
                f"Device: {config.deviceName}\n"
                f"Platform Version: {config.platformVersion}",
                name='Configuration',
                attachment_type=allure.attachment_type.TEXT
            )

            options.set_capability('bstack:options', {
                'projectName': 'Litres autotest project',
                'buildName': 'litres-build-1',
                'sessionName': 'BStack litres_test',
                'userName': config.bstack_userName,
                'accessKey': config.bstack_accessKey,
            })

        with allure.step('Инициализация сессии'):
            browser.config.driver = webdriver.Remote(
                config.remote_url,
                options=options
            )

        browser.config.timeout = config.timeout
        browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )

        yield

    except Exception as e:
        allure.attach(
            str(e),
            name='Error Details',
            attachment_type=allure.attachment_type.TEXT
        )
        raise

    finally:
        if hasattr(browser, 'driver'):
            session_id = browser.driver.session_id
            add_mobile_screenshot(browser)
            add_mobile_xml(browser)

            with allure.step('End session'):
                browser.quit()

            if config.context == 'bstack':
                add_mobile_bstack_video(session_id)
