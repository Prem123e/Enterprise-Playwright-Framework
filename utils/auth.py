class AuthManager:

    def __init__(self):
        self.token=None

    def set_token(self,token:str):
        self.token=token

    def get_auth_headers(self):
        return{
            "Authorization": f"Bearer {self.token}"
        }