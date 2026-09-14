import requests
from config.config import API_BASE_URL

class APIClient:

    def __init__(self):
        self.base_url=API_BASE_URL
    def get(self, endpoint: str, params=None, headers=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            params=params,
            headers=headers
        )

    def post(self, endpoint: str, data: dict, headers=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def put(self, endpoint: str, data: dict, headers=None):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def patch(self, endpoint: str, data: dict, headers=None):
        return requests.patch(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def delete(self, endpoint: str, headers=None):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )