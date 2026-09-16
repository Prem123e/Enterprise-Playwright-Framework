from utils.auth import AuthManager
from api.api_client import APIClient
from config.config import API_TOKEN
from utils.api_assertions import (
    assert_status_code,
    assert_json_field
)


def test_generate_auth_headers():

    auth = AuthManager()

    auth.set_token(API_TOKEN)

    headers = auth.get_auth_headers()

    assert headers["Authorization"] == "Bearer ABC123"

    print(headers)


def test_authenticated_api_request():

    auth = AuthManager()

    auth.set_token("ABC123")

    headers = auth.get_auth_headers()

    client = APIClient()

    response = client.get(
    "/posts/1",
    headers=headers
    )

    assert_status_code(response, 200)
    assert_json_field(response, "id", 1)

    print(response.json())