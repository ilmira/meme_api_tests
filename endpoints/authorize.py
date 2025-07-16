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
        Endpoint.user = name
        Endpoint.token = self.response.json()['token']

    @allure.step('Set headers for authorization')
    def set_headers_with_token(self):
        Endpoint.headers = {'Authorization': self.token}
