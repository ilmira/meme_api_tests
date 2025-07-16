from endpoints.endpoint import Endpoint
import allure
import requests


class DeleteMeme(Endpoint):
    @allure.step('Delete meme')
    def delete_meme(self, id):
        self.response = requests.get(f'{self.url}/meme/{id}', headers=self.headers)
        self.json = self.response.json()