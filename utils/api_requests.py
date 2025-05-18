import requests
import allure
import logging
from allure_commons.types import AttachmentType
from tests.api.conftest import base_url
from utils.logging_helper import logging_helper


def api_get(url, **kwargs):
    with allure.step("API Request"):
        result = requests.get(base_url + url, **kwargs)
        logging_helper(result)
        return result


def api_post(url, **kwargs):
    with allure.step("API Request"):
        result = requests.post(base_url + url, **kwargs)
        logging_helper(result)
        return result


def api_put(url, **kwargs):
    with allure.step("API Request"):
        result = requests.put(base_url + url, **kwargs)
        logging_helper(result)
        return result


def api_put_to_wishlist(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.put(url='https://api.litres.ru/foundation/api/' + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=str(result.status_code), name='Status Code',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(result.request.url)
        logging.info(result.status_code)
    return result


def api_delete(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.delete(url='https://api.litres.ru/foundation/api/' + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=str(result.status_code), name='Status Code',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(result.request.url)
        logging.info(result.status_code)
    return result