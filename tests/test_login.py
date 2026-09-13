import os
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import load_test_data
from config.config import BASE_URL
def test_login_with_valid_credentials(page):
    data = load_test_data(
    os.path.join("data", "test_data.json")
    )
    login_data = data["valid_login"]
    checkout_data = data["checkout_customer"]
    product_data = data["product"]
    login_page=LoginPage(page)
    product_page=ProductsPage(page)
    cart_page=CartPage(page)
    checkout_page=CheckoutPage(page)
    login_page.open()
    login_page.login(
        login_data["username"],
        login_data["password"]
    )
    expect(page).to_have_url(
    f"{BASE_URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")
    product_count=product_page.get_product_count()
    print(product_count)
    assert product_count == 6
    product_page.add_product_to_cart(product_data["name"])
    expect(
        page.get_by_role("button", name="Remove")
    ).to_be_visible()
    cart_page.open()
    assert cart_page.get_cart_item_count() == 1
    cart_page.verify_product(product_data["name"])
    checkout_page.open()
    checkout_page.verify_checkout_page()
    checkout_page.enter_customer_details(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )
    checkout_page.continue_checkout()
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    
    