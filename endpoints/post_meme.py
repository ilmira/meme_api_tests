from endpoints.endpoint import Endpoint
import allure
import requests


class PostMeme(Endpoint):
    @allure.step('Post meme')
    def post_meme(self, body):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)
        self.json = self.response.json()
        return self.response