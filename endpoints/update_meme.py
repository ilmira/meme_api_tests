from endpoints.authorize import Authorize
from endpoints.endpoint import Endpoint
import allure
import requests


class UpdateMeme(Endpoint):
    @allure.step('Update meme by id')
    def update_meme_by_id(self, id, body, set_headers=True, headers=None):
        if set_headers:
            if not headers:
                headers = self.headers
            self.response = requests.put(f'{self.url}/meme/{id}', json=body, headers=headers)
            try:
                self.json = self.response.json()
                return self.response
            except Exception:
                return self.response
        else:
            self.response = requests.put(f'{self.url}/meme/{id}', json=body)
            return self.response


    @allure.step('Update meme by id: not valid, wrong user')
    def update_meme_by_id_wrong_user(self, id, body):
        headers = Authorize.get_token_another_user(Authorize(), 'Another user')
        self.update_meme_by_id(id, body, headers=headers)
