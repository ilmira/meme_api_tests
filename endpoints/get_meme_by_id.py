from endpoints.authorize import Authorize
from endpoints.endpoint import Endpoint
import allure
import requests


class GetMemeById(Endpoint):
    @allure.step('Get meme by id')
    def get_meme_by_id(self, id):
        self.response = requests.get(f'{self.url}/meme/{id}', headers=self.headers)
        self.json = self.response.json()
        return self.response

    @allure.step('Get meme by id: wrong id')
    def get_meme_by_id_wrong_id(self, id):
        self.response = requests.get(f'{self.url}/meme/{id}', headers=self.headers)
        return self.response

    @allure.step('Get meme by id: not valid, unauthorized user')
    def get_meme_by_id_unauthorised(self, id):
        self.response = requests.get(f'{self.url}/meme/{id}')
        return self.response

    @allure.step('Get meme by id: not valid, wrong user')
    def get_meme_by_id_wrong_user(self, id):
        headers = Authorize.get_token_another_user(Authorize(), 'Another user')
        self.response = requests.get(f'{self.url}/meme/{id}', headers=headers)
        self.json = self.response.json()
        return self.response
