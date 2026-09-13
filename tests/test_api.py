from api.api_client import APIClient

client = APIClient()
def test_get_single_post():
    response = client.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200
    response_data = response.json()

    assert response_data["id"] == 1

    print(response_data)

def test_create_post():

    payload = {
        "title": "API Automation",
        "body": "Learning POST requests",
        "userId": 1
    }

    response = client.post(
        "https://jsonplaceholder.typicode.com/posts",
        payload
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["title"] == "API Automation"
    assert response_data["body"] == "Learning POST requests"
    assert response_data["userId"] == 1

    print(response_data)