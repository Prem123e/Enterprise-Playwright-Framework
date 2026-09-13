import requests

class APIClient:

    def get(self,url:str):
        return requests.get(url)

    def post(self,url:str,data:dict):
        return requests.post(url,json=data)