from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,page:Page):
        super().__init__(page)

    def open(self):
        self.navigate("https://www.saucedemo.com/")

    def login(self,username:str,password:str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
    