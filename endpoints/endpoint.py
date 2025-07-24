import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    user = "Ilmira"
    token = None
    headers = None

    @allure.step('Data is correct')
    def check_data(self, data, data_name):
        assert 'id' in self.json
        assert self.json['id']
        assert self.json['updated_by'] == self.user
        assert self.json[data_name] == data

    @allure.step('Check status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, f'Status code is "{self.response.status_code}", not 200!'

    @allure.step('Check status code is 401')
    def check_status_code_is_401(self):
        assert self.response.status_code == 401, f'Status code is "{self.response.status_code}", not 401!'

    @allure.step('Check status code is 403')
    def check_status_code_is_403(self):
        assert self.response.status_code == 403, f'Status code is "{self.response.status_code}", not 403!'

    @allure.step('Check status code is 404')
    def check_status_code_is_404(self):
        assert self.response.status_code == 404, f'Status code is "{self.response.status_code}", not 404!'

    @allure.step('Check status code is 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, f'Status code is "{self.response.status_code}", not 400!'

    @allure.step('Check requirements fields')
    def check_requirements_fields(self, url):
        requirements = ['text', 'url', 'tags', 'info']
        missing = requirements - self.json.keys()
        assert not missing, f'There is missing fields: {missing}'
