import requests

class APIClient:

    def get(self,url:str):
        return requests.get(url)

    def post(self,url:str,data:dict):
        return requests.post(url,json=data)
    def put(self,url:str,data:dict):
        return requests.put(url,json=data)
    def patch(self,url:str,data:dict):
        return requests.patch(url,json=data)
    def delete(self,url:str):
        return requests.delete(url)