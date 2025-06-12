import requests
import allure
import logging
from allure_commons.types import AttachmentType
from helpers.utils.logging_helper import logging_helper
from config import config

API_PATH = '/foundation/api'

def _build_url(endpoint: str) -> str:
    return f"{config.base_api_url}{API_PATH}{endpoint}"

def api_get(endpoint, **kwargs):
    with allure.step("API GET Request"):
        url = _build_url(endpoint)
        result = requests.get(url, **kwargs)
        logging_helper(result)
        return result


def api_post(endpoint, **kwargs):
    with allure.step("API POST Request"):
        url = _build_url(endpoint)
        result = requests.post(url, **kwargs)
        logging_helper(result)
        return result


def api_put(endpoint, **kwargs):
    with allure.step("API PUT Request"):
        url = _build_url(endpoint)
        result = requests.put(url, **kwargs)
        logging_helper(result)
        return result


def api_put_to_wishlist(endpoint, **kwargs):
    with allure.step('API PUT Request'):
        url = _build_url(endpoint)
        result = requests.put(url, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=str(result.status_code), name='Status Code',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(result.request.url)
        logging.info(result.status_code)
    return result


def api_delete(endpoint, **kwargs):
    with allure.step('API DELETE Request'):
        url = _build_url(endpoint)
        result = requests.delete(url, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=str(result.status_code), name='Status Code',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(result.request.url)
        logging.info(result.status_code)
    return result