from endpoints.endpoint import Endpoint
import allure
import requests


class UpdateMeme(Endpoint):
    @allure.step('Get all memes')
    def update_meme_by_id(self, id, body):
        self.response = requests.put(f'{self.url}/meme/{id}', json=body, headers=self.headers)
        self.json = self.response.json()
        return self.response
