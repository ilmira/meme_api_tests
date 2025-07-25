import pytest
import allure

bodies = [{
    'text': 'no stress',
    'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
    'tags': ['cat', 'stress', 'vibe'],
    'info': {"colors": "white"}
},
    {
        'text': 'smth wrong',
        'url': 'https://news.store.rambler.ru/img/9dd07f9efa5d53d64aa28990a7e87768?img-format=auto&img-1-resize=height:400,fit:max&img-2-filter=sharpen',
        'tags': ['wait', 'girly', 'russian'],
        'info': {"colors": "blue"}
    },
    {
        'text': 'its memes',
        'url': 'https://lh7-us.googleusercontent.com/docsz/AD_4nXchN7kVpPlp4U1HX5IPaeoQTLrFxRt6LHFdkwGsATTZ96UViEKyB2zypdFqUH5x4dffkSTPJfEAN9POtmoKHAbqMsyyMnM1H5hMZPjOx3mXd2hBfiIGIx6FPAAEPygDF-3NYllGBz8YvdHzHy246_om3rw3?key=Q7p1Upwig0RrmmOArNZ42Q',
        'tags': ['meme', 'russian'],
        'info': {"colors": "black"}
    }
]


@allure.title('Check authorization')
@allure.feature('Authorization')
@allure.story('Get token')
@pytest.mark.critical
def test_get_authorize_token(authorize):
    authorize.check_status_code_is_200()
    authorize.check_data(authorize.user, "user")
    authorize.check_data(authorize.token, 'token')
    authorize.check_token_is_good()


@allure.title('Check authorization')
@allure.feature('Authorization')
@allure.story('Check token')
@pytest.mark.critical
def test_check_authorize_token(authorize_token):
    authorize_token.check_status_code_is_200()
    authorize_token.check_token_is_alive()
    authorize_token.check_data()


@allure.title('Post new meme')
@allure.feature('Add/update memes')
@allure.story('Add meme')
@pytest.mark.critical
@pytest.mark.parametrize('body', bodies)
def test_post_meme(post_endpoint, body):
    post_endpoint.post_meme(body)
    post_endpoint.check_status_code_is_200()
    post_endpoint.check_data(body['text'], 'text')
    post_endpoint.check_data(body['url'], 'url')
    post_endpoint.check_data(body['tags'], 'tags')
    post_endpoint.check_data(body['info'], 'info')


@allure.title('Post new meme: wrong data')
@allure.feature('Add/update memes')
@allure.story('Add meme')
@pytest.mark.critical
def test_post_meme_wrong_data(post_endpoint):
    body = {
        'text': 1556,
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }
    post_endpoint.post_meme(body)
    post_endpoint.check_status_code_is_400()


@allure.title('Post new meme: wrong data: without url')
@allure.feature('Add/update memes')
@allure.story('Add meme')
@pytest.mark.critical
def test_post_meme_wrong_data_without_url(post_endpoint):
    body = {
        'text': 'no stress',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }
    post_endpoint.post_meme(body)
    post_endpoint.check_status_code_is_400()


@allure.title('Post new meme: unauthorized user')
@allure.feature('Add/update memes')
@allure.story('Add meme')
@pytest.mark.critical
def test_post_meme_unauthorized(post_endpoint):
    body = {
        'text': 'no stress',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }
    post_endpoint.post_meme(body, set_headers=False)
    post_endpoint.check_status_code_is_401()


@allure.title('Get all memes')
@allure.feature('Get memes')
@allure.story('Get all memes')
@pytest.mark.critical
def test_get_all_memes(get_memes_endpoint):
    get_memes_endpoint.get_memes()
    get_memes_endpoint.check_status_code_is_200()
    get_memes_endpoint.check_data()


@allure.title('Get all memes')
@allure.feature('Get memes')
@allure.story('Get all memes: unauthorized user')
@pytest.mark.critical
def test_get_all_memes_unauthorized(get_memes_endpoint):
    get_memes_endpoint.get_memes(set_headers=False)
    get_memes_endpoint.check_status_code_is_401()


@allure.title('Get meme by id')
@allure.feature('Get memes')
@allure.story('Get meme by id')
@pytest.mark.critical
def test_get_meme_by_id(new_meme_id, get_meme_by_id_endpoint):
    get_meme_by_id_endpoint.get_meme_by_id(new_meme_id)
    get_meme_by_id_endpoint.check_status_code_is_200()
    get_meme_by_id_endpoint.check_data(new_meme_id, 'id')


@allure.title('Get meme by id: unauthorized user')
@allure.feature('Get memes')
@allure.story('Get meme by id')
@pytest.mark.critical
def test_get_meme_by_id_unauthorized(new_meme_id, get_meme_by_id_endpoint):
    get_meme_by_id_endpoint.get_meme_by_id(new_meme_id, set_headers=False)
    get_meme_by_id_endpoint.check_status_code_is_401()


@allure.title('Get meme by id: meme by wrong user')
@allure.feature('Get memes')
@allure.story('Get meme by id')
@pytest.mark.critical
def test_get_meme_by_id_wrong_user(new_meme_id, get_meme_by_id_endpoint, authorize):
    get_meme_by_id_endpoint.get_meme_by_id_wrong_user(new_meme_id)
    get_meme_by_id_endpoint.check_status_code_is_200()


@allure.title('Get meme by id: wrong id')
@allure.feature('Get memes')
@allure.story('Get meme by id')
@pytest.mark.critical
def test_get_meme_by_id_wrong_id(get_meme_by_id_endpoint):
    get_meme_by_id_endpoint.get_meme_by_id(1000000000000000000000)
    get_meme_by_id_endpoint.check_status_code_is_404()


@allure.title('Update meme')
@allure.feature('Add/update memes')
@allure.story('Update meme')
@pytest.mark.medium
def test_put_meme(new_meme_id, put_endpoint):
    body = {
        'id': new_meme_id,
        'text': 'no stress UPD',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }

    put_endpoint.update_meme_by_id(new_meme_id, body)
    put_endpoint.check_status_code_is_200()
    put_endpoint.check_data(body['text'], 'text')
    put_endpoint.check_data(body['url'], 'url')
    put_endpoint.check_data(body['tags'], 'tags')
    put_endpoint.check_data(body['info'], 'info')


@allure.title('Update meme: wrong data')
@allure.feature('Add/update memes')
@allure.story('Update meme')
@pytest.mark.medium
def test_put_meme_wrong_data(new_meme_id, put_endpoint):
    body = {
        'id': new_meme_id,
        'text': 'no stress UPD',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': "white"
    }

    put_endpoint.update_meme_by_id(new_meme_id, body)
    put_endpoint.check_status_code_is_400()


@allure.title('Update meme: wrong data: without id')
@allure.feature('Add/update memes')
@allure.story('Update meme')
@pytest.mark.medium
def test_put_meme_wrong_data_without_id(new_meme_id, put_endpoint):
    body = {
        'text': 'no stress UPD',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }

    put_endpoint.update_meme_by_id(new_meme_id, body)
    put_endpoint.check_status_code_is_400()


@allure.title('Update meme: unauthorized user')
@allure.feature('Add/update memes')
@allure.story('Update meme')
@pytest.mark.medium
def test_put_meme_unauthorized(new_meme_id, put_endpoint):
    body = {
        'id': new_meme_id,
        'text': 'no stress UPD',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }
    put_endpoint.update_meme_by_id(new_meme_id, body, set_headers=False)
    put_endpoint.check_status_code_is_401()


@allure.title('Update meme: by wrong user')
@allure.feature('Add/update memes')
@allure.story('Update meme')
@pytest.mark.medium
def test_put_meme_wrong_user(new_meme_id, put_endpoint):
    body = {
        'id': new_meme_id,
        'text': 'no stress UPD',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }

    put_endpoint.update_meme_by_id_wrong_user(new_meme_id, body)
    put_endpoint.check_status_code_is_403()


@allure.title('Delete meme')
@allure.feature('Delete memes')
@allure.story('Delete meme')
def test_delete_meme(new_meme_id, delete_endpoint):
    delete_endpoint.delete_meme(new_meme_id)
    delete_endpoint.check_status_code_is_200()
    delete_endpoint.check_data(new_meme_id)
    delete_endpoint.check_that_meme_is_deleted(new_meme_id)


@allure.title('Delete meme: unauthorized user')
@allure.feature('Delete memes')
@allure.story('Delete meme')
def test_delete_meme_unauthorised(new_meme_id, delete_endpoint):
    delete_endpoint.delete_meme(new_meme_id, set_headers=False)
    delete_endpoint.check_status_code_is_401()


@allure.title('Delete meme: by wrong user')
@allure.feature('Delete memes')
@allure.story('Delete meme')
def test_delete_meme_wrong_user(new_meme_id, delete_endpoint):
    delete_endpoint.delete_meme_wrong_user(new_meme_id)
    delete_endpoint.check_status_code_is_403()
