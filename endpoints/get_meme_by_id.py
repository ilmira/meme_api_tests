from endpoints.endpoint import Endpoint
import allure
import requests


class GetMemeById(Endpoint):
    @allure.step('Get meme by id')
    def get_meme_by_id(self, id):
        self.response = requests.get(f'{self.url}/meme/{id}', headers=self.headers)
        self.json = self.response.json()
        return self.response
