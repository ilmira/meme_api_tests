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


@allure.title('Post new meme')
@allure.feature('Add/update memes')
@allure.story('Add meme')
@pytest.mark.critical
@pytest.mark.parametrize('body', bodies)
def test_post_meme(post_endpoint, authorization, body):
    authorization('Ilmira')
    post_endpoint.post_meme(body)
    post_endpoint.check_status_code_is_200()
    post_endpoint.check_data(body['url'], 'url')

@allure.title('Get all memes')
@allure.feature('Get memes')
@allure.story('Get all memes')
@pytest.mark.critical
def test_get_all_memes(get_memes_endpoint, authorization):
    authorization('Ilmira')
    get_memes_endpoint.get_memes()
    get_memes_endpoint.check_status_code_is_200()

@allure.title('Get all memes')
@allure.feature('Get memes')
@allure.story('Get meme by id')
@pytest.mark.critical
def test_get_meme_by_id(new_meme_id, get_meme_by_id_endpoint, authorization):
    authorization('Ilmira')
    get_meme_by_id_endpoint.get_meme_by_id(new_meme_id)
    get_meme_by_id_endpoint.check_status_code_is_200()
    get_meme_by_id_endpoint.check_data(new_meme_id, 'id')

@allure.title('Update meme')
@allure.feature('Add/update memes')
@allure.story('Update meme')
@pytest.mark.medium
def test_put_meme(new_meme_id, put_endpoint, authorization):
    body = {
        'id': new_meme_id,
        'text': 'no stress UPD',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }
    authorization('Ilmira')
    put_endpoint.update_meme_by_id(new_meme_id, body)
    put_endpoint.check_status_code_is_200()
    put_endpoint.check_data(body['text'], 'text')


@allure.title('Delete meme')
@allure.feature('Delete memes')
@allure.story('Delete meme')
def test_delete_meme(new_meme_id, delete_endpoint, authorization):
    authorization('Ilmira')
    delete_endpoint.delete_meme(new_meme_id)
    delete_endpoint.check_status_code_is_200()
