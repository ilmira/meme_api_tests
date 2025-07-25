from json import JSONDecodeError

from endpoints.authorize import Authorize
from endpoints.endpoint import Endpoint
import allure
import requests


class GetMemeById(Endpoint):
    @allure.step('Get meme by id')
    def get_meme_by_id(self, id, set_headers=True, headers=None):
        if set_headers:
            if not headers:
                headers = self.headers
            self.response = requests.get(f'{self.url}/meme/{id}', headers=headers)
            try:
                self.json = self.response.json()
                return self.response
            except JSONDecodeError:
                return self.response
        else:
            self.response = requests.get(f'{self.url}/meme/{id}')
            return self.response

    @allure.step('Get meme by id: not valid, wrong user')
    def get_meme_by_id_wrong_user(self, id):
        headers = Authorize.get_token_another_user(Authorize(), 'Another user')
        self.get_meme_by_id(id, headers=headers)
