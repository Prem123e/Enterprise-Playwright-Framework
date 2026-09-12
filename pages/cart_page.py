from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self,page:Page):
        self.page=page
        super().__init__(page)

    def open(self):
        self.page.locator(".shopping_cart_container").click()

    def get_cart_item_count(self):
        return self.page.locator(".cart_item").count()
    def verify_product(self,product_name:str):
        expect(
            self.page.locator(".cart_item")).to_contain_text(product_name)
