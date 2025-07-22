from endpoints.endpoint import Endpoint
import allure
import requests


class GetMemes(Endpoint):
    @allure.step('Get all memes')
    def get_memes(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        self.json = self.response.json()
        return self.response

    @allure.step('Get all memes: not valid, unauthorized user')
    def get_memes_unauthorised(self):
        self.response = requests.get(f'{self.url}/meme')
        return self.response
