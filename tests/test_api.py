from api.api_client import APIClient
def test_get_single_post():
    client = APIClient()
    response = client.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200
    response_data = response.json()

    assert response_data["id"] == 1

    print(response_data)

def test_create_post():
    client = APIClient()
    original_payload = {
        "title": "API Automation",
        "body": "Learning POST requests",
        "userId": 1
    }
    response = client.post(
        "https://jsonplaceholder.typicode.com/posts",
        original_payload
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["title"] == "API Automation"
    assert response_data["body"] == "Learning POST requests"
    assert response_data["userId"] == 1

    print(response_data)

def test_update_post_with_put():
    client = APIClient()
    payload = {
        "id": 1,
        "title": "Updated API Automation",
        "body": "Updated using PUT",
        "userId": 1
    }
    response=client.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        payload
    )
    assert response.status_code== 200
    response_data=response.json()
    assert response_data["id"] == 1
    assert response_data["title"] == "Updated API Automation"
    assert response_data["body"] == "Updated using PUT"
    print(response_data)

def test_update_post_with_patch():
    client = APIClient()
    payload = {
        "title": "Partially Updated Title"
    }
    response=client.patch("https://jsonplaceholder.typicode.com/posts/1",payload)
    assert response.status_code== 200
    response_data=response.json()
    assert response_data["id"] == 1
    assert response_data["title"] == "Partially Updated Title"

    print(response_data)

def test_delete_post():
    client = APIClient()
    response=client.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

    print(response.status_code)