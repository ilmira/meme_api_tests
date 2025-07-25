from endpoints.endpoint import Endpoint
import allure
import requests


class PostMeme(Endpoint):
    @allure.step('Post meme')
    def post_meme(self, body, set_headers=True):
        if set_headers:
            self.response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)
            try:
                self.json = self.response.json()
                return self.response
            except Exception:
                return self.response
        else:
            self.response = requests.post(f'{self.url}/meme', json=body)
            return self.response
