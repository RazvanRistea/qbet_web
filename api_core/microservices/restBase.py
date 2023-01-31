import allure
import requests

import logging


class ApiClient:

    def __init__(self):
        pass

    logger = logging.getLogger(__name__)

    def post(self, base_address=None, path=None, params=None, data=None, json=None, headers=None):
        url = f"{base_address}{path}"
        with allure.step(f'POST request to: {url}'):
            self.logger.info(f'POST request to: {url}')
            self.logger.debug(f'JSON body: {json}')
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def put(self, base_address=None, path=None, params=None, data=None, json=None, headers=None):
        url = f"{base_address}{path}"
        with allure.step(f'PUT request to: {url}'):
            self.logger.info(f'PUT request to: {url}')
            self.logger.debug(f'JSON body: {json}')
            return requests.put(url=url, params=params, data=data, json=json, headers=headers)

    def patch(self, base_address=None, path=None, params=None, data=None, json=None, headers=None):
        url = f"{base_address}{path}"
        with allure.step(f'PATCH request to: {url}'):
            self.logger.info(f'PATCH request to: {url}')
            self.logger.debug(f'JSON body: {json}')
            return requests.patch(url=url, params=params, data=data, json=json, headers=headers)

    def get(self, base_address=None, path=None, params=None, headers=None):
        url = f"{base_address}{path}"
        with allure.step(f'GET request to: {url}'):
            self.logger.info(f'GET request to: {url}')
            return requests.get(url=url, params=params, headers=headers)

    def delete(self, base_address=None, path=None, params=None, headers=None):
        url = f"{base_address}{path}"
        with allure.step(f'DELETE request to: {url}'):
            self.logger.info(f'DELETE request to: {url}')
            return requests.delete(url=url, params=params, headers=headers)
