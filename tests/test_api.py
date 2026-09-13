from api.api_client import APIClient

def test_get_single():
    client=APIClient()

    response=client.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    response_data=response.json()
    assert response_data["id"]== 1
    print(response_data)