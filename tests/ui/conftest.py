import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from helpers.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', help='Browser version Selenoid', default='128.0'
    )
    parser.addoption(
        '--local', action='store_true', help='Run tests in a local browser'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setting_browser(request):
    is_local = request.config.getoption('--local')
    browser_version = request.config.getoption('--browser_version')

    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    options = Options()

    if is_local:
        # Локальный браузер
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
    else:
        # Selenoid
        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': browser_version,
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }

        selenoid_login = os.getenv('SELENOID_LOGIN')
        selenoid_pass = os.getenv('SELENOID_PASS')
        selenoid_url = os.getenv('SELENOID_URL')

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
            options=options
        )


    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    driver.implicitly_wait(10)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if not is_local:
        attach.add_video(browser)

    browser.quit()