from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.product_page import ProductsPage

def test_login_with_valid_credentials(page):

    login_page=LoginPage(page)
    product_page=ProductsPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")
    product_count=product_page.get_product_count()
    print(product_count)
    assert product_count == 6
    product_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    expect(
        page.get_by_role("button", name="Remove")
    ).to_be_visible()
    