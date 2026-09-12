from playwright.sync_api import Page

class BasePage:

    def __init__(self,page:Page):
        self.page=page

    def navigate(self, url):
        self.page.goto(url)

    def get_page_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url

    def wait_for_pageload(self):
        self.page.wait_for_load_state('networkidle')

    def refresh_page(self):
        self.page.reload()

    