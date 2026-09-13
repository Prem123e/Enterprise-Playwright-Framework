import requests


class APIClient:

    def get(self, url: str, params=None, headers=None):
        return requests.get(
            url,
            params=params,
            headers=headers
        )

    def post(self, url: str, data: dict, headers=None):
        return requests.post(
            url,
            json=data,
            headers=headers
        )

    def put(self, url: str, data: dict, headers=None):
        return requests.put(
            url,
            json=data,
            headers=headers
        )

    def patch(self, url: str, data: dict, headers=None):
        return requests.patch(
            url,
            json=data,
            headers=headers
        )

    def delete(self, url: str, headers=None):
        return requests.delete(
            url,
            headers=headers
        )