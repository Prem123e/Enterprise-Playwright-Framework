from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_with_valid_credentials(page):

    login_page=LoginPage(page)
    login_page.navigate()
    print(page.url)
    print(page.title())
    login_page.login("standard_user","secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


