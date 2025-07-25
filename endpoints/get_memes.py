from endpoints.endpoint import Endpoint
import allure
import requests


class GetMemes(Endpoint):
    @allure.step('Get all memes')
    def get_memes(self, set_headers=True):
        if set_headers:
            self.response = requests.get(f'{self.url}/meme', headers=self.headers)
            self.json = self.response.json()
            return self.response
        else:
            self.response = requests.get(f'{self.url}/meme')
            return self.response

    @allure.step('Check data')
    def check_data(self):
        assert self.json
