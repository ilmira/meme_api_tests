from endpoints.endpoint import Endpoint
import requests
import allure


class Authorize(Endpoint):

    @allure.step('Get token for authorization')
    def get_token(self, name):
        body = {
            "name": name
        }
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        Endpoint.user = name
        Endpoint.token = self.response.json()['token']

    @allure.step('Set headers for authorization')
    def set_headers_with_token(self):
        Endpoint.headers = {'Authorization': self.token}

    @allure.step('Data is correct')
    def check_data(self, data, data_name):
        assert self.json[data_name] == data

    @allure.step('Check token is good')
    def check_token_is_good(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        assert self.response.status_code == 200, f'Status code is {self.response.status_code}, not 200! Token is not good!'
