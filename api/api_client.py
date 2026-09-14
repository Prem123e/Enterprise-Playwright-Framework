import requests

from config.config import API_BASE_URL


class APIClient:

    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def request(
        self,
        method: str,
        endpoint: str,
        params=None,
        data=None,
        headers=None
    ):
        return self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            params=params,
            json=data,
            headers=headers
        )

    def get(self, endpoint: str, params=None, headers=None):
        return self.request(
            "GET",
            endpoint,
            params=params,
            headers=headers
        )

    def post(self, endpoint: str, data: dict, headers=None):
        return self.request(
            "POST",
            endpoint,
            data=data,
            headers=headers
        )

    def put(self, endpoint: str, data: dict, headers=None):
        return self.request(
            "PUT",
            endpoint,
            data=data,
            headers=headers
        )

    def patch(self, endpoint: str, data: dict, headers=None):
        return self.request(
            "PATCH",
            endpoint,
            data=data,
            headers=headers
        )

    def delete(self, endpoint: str, headers=None):
        return self.request(
            "DELETE",
            endpoint,
            headers=headers
        )