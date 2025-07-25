from email.feedparser import headerRE

from endpoints.authorize import Authorize
from endpoints.endpoint import Endpoint
import allure
import requests


class DeleteMeme(Endpoint):
    @allure.step('Delete meme')
    def delete_meme(self, id, set_headers=True, headers=None):
        if set_headers:
            headers = headers if headers is not None else self.headers
        else:
            headers = {}
        self.response = requests.delete(f'{self.url}/meme/{id}', headers=headers)

    @allure.step('Check data')
    def check_data(self, id):
        assert self.response.text == f'Meme with id {id} successfully deleted', f'Text is: {self.response.text}'

    @allure.step('Check that meme is deleted')
    def check_that_meme_is_deleted(self, id):
        self.response = requests.get(f'{self.url}/meme/{id}', headers=self.headers)
        assert self.response.status_code == 404, f'Status code is not 404, its {self.response.status_code}'

    @allure.step('Delete meme: by wrong user')
    def delete_meme_wrong_user(self, id):
        headers = Authorize.get_token_another_user(Authorize(), 'Another user')
        self.delete_meme(id, headers=headers)
