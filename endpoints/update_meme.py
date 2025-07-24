from endpoints.authorize import Authorize
from endpoints.endpoint import Endpoint
import allure
import requests


class UpdateMeme(Endpoint):
    @allure.step('Update meme by id')
    def update_meme_by_id(self, id, body):
        self.response = requests.put(f'{self.url}/meme/{id}', json=body, headers=self.headers)
        self.json = self.response.json()
        return self.response

    @allure.step('Update meme by id: wrong data')
    def update_meme_by_id_wrong_data(self, id, body):
        self.response = requests.put(f'{self.url}/meme/{id}', json=body, headers=self.headers)
        return self.response

    @allure.step('Update meme by id: not valid, wrong user')
    def update_meme_by_id_wrong_user(self, id, body):
        headers = Authorize.get_token_another_user(Authorize(), 'Another user')
        self.response = requests.put(f'{self.url}/meme/{id}', json=body, headers=headers)
        return self.response

    @allure.step('Update meme by id: not valid, unauthorised')
    def update_meme_by_id_unauthorised(self, id, body):
        self.response = requests.put(f'{self.url}/meme/{id}', json=body)
        return self.response
