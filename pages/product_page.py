from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    def get_product_count(self):
        return self.page.locator(".inventory_item").count()

    def add_product_to_cart(self,product_name:str):
        product=self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.get_by_role("button",name="Add to cart").click()
