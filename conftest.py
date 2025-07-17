import pytest
from endpoints.authorize import Authorize
from endpoints.authorize_token import AuthorizeToken
from endpoints.delete_meme import DeleteMeme
from endpoints.get_memes import GetMemes
from endpoints.get_meme_by_id import GetMemeById
from endpoints.post_meme import PostMeme
from endpoints.update_meme import UpdateMeme

@pytest.fixture()
def authorize():
    return Authorize()

@pytest.fixture()
def authorize_token():
    return AuthorizeToken()

@pytest.fixture()
def get_memes_endpoint():
    return GetMemes()

@pytest.fixture()
def get_meme_by_id_endpoint():
    return GetMemeById()

@pytest.fixture()
def post_endpoint():
    return PostMeme()

@pytest.fixture()
def put_endpoint():
    return UpdateMeme()

@pytest.fixture()
def delete_endpoint():
    return DeleteMeme()

@pytest.fixture(autouse=True)
def authorization(authorize, authorize_token):
    if not authorize_token.check_token_is_alive():
        authorize.get_token("Ilmira")
        authorize.set_headers_with_token()

@pytest.fixture()
def new_meme_id(post_endpoint, delete_endpoint):
    body = {
        'text': 'no stress',
        'url': 'https://img.freepik.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740',
        'tags': ['cat', 'stress', 'vibe'],
        'info': {"colors": "white"}
    }
    meme_id = post_endpoint.post_meme(body).json()['id']
    yield meme_id
    delete_endpoint.delete_meme(meme_id)
