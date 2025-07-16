from endpoints.endpoint import Endpoint
import allure
import requests


class AuthorizeToken(Endpoint):
    @allure.step('Check: token for authorization is alive')
    def check_token_is_alive(self):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        if self.response.text == f'Token is alive. Username is {self.user}':
            return True
        else:
            return False
