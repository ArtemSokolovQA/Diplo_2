import requests
import pytest
import allure

import config
import data


class StellarBurgersApi:

    @staticmethod
    @allure.step('Отправить запрос на регистрацию пользователя')
    def create_user(body):
        return requests.post(f'{config.Urls.BASE_URL}{config.Urls.CREATE_USER_PATH}',
                             json=body)

    @staticmethod
    @allure.step('Отправить запрос на удаление пользователя')
    def delete_user(token):
        return requests.delete(f'{config.Urls.BASE_URL}{config.Urls.DELETE_USER_PATH}', headers={
            'Authorization': token
        })

    @staticmethod
    @allure.step('Отправить запрос на авторизацию пользователя')
    def auth(email, password):
        return requests.post(f'{config.Urls.BASE_URL}{config.Urls.AUTH_PATH}', json={
            "email": email,
            "password": password
        })
