from playwright.sync_api import Page, expect

def test_open_saucedemo(page:Page):

    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    print(page.title())
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(5000)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")
    print(page.locator(".inventory_item").count())


