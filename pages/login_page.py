from playwright.sync_api import Page

class LoginPage:

    def __init__(self,page:Page):
        self.page=page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self,username,password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_timeout(5000)
    