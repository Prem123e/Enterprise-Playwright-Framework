from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

    def open(self):
        self.page.get_by_role("button",name="Checkout").click()
    def verify_checkout_page(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Your Information")
    def enter_customer_details(self,
        first_name: str,
        last_name: str,
        postal_code: str):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("Zip/Postal Code").fill(postal_code)
    def continue_checkout(self):
        self.page.get_by_role("button",name="Continue").click()