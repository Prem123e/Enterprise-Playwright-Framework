from utils.api_assertions import (
    assert_status_code,
    assert_json_field
)


def test_get_single_post(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert_status_code(response, 200)
    assert_json_field(response, "id", 1)

    print(response.json())


def test_create_post(api_client):

    payload = {
        "title": "API Automation",
        "body": "Learning POST requests",
        "userId": 1
    }

    response = api_client.post(
        "https://jsonplaceholder.typicode.com/posts",
        payload
    )

    assert_status_code(response, 201)

    assert_json_field(
        response,
        "title",
        "API Automation"
    )

    assert_json_field(
        response,
        "body",
        "Learning POST requests"
    )

    assert_json_field(
        response,
        "userId",
        1
    )

    print(response.json())


def test_update_post_with_put(api_client):

    payload = {
        "id": 1,
        "title": "Updated API Automation",
        "body": "Updated using PUT",
        "userId": 1
    }

    response = api_client.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        payload
    )

    assert_status_code(response, 200)

    assert_json_field(response, "id", 1)

    assert_json_field(
        response,
        "title",
        "Updated API Automation"
    )

    assert_json_field(
        response,
        "body",
        "Updated using PUT"
    )

    print(response.json())


def test_update_post_with_patch(api_client):

    payload = {
        "title": "Partially Updated Title"
    }

    response = api_client.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        payload
    )

    assert_status_code(response, 200)

    assert_json_field(response, "id", 1)

    assert_json_field(
        response,
        "title",
        "Partially Updated Title"
    )

    print(response.json())


def test_delete_post(api_client):

    response = api_client.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert_status_code(response, 200)

    print(response.status_code)


def test_get_posts_by_user(api_client):

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": 1}
    )

    assert_status_code(response, 200)

    response_data = response.json()

    assert len(response_data) > 0

    for post in response_data:
        assert post["userId"] == 1

    print(response_data)


def test_get_post_with_headers(api_client):

    headers = {
        "Accept": "application/json"
    }

    response = api_client.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers
    )

    assert_status_code(response, 200)

    assert_json_field(response, "id", 1)

    print(response.json())