from playwright.sync_api import Page, expect

def test_open_saucedemo(page:Page):

    page.goto("https://www.saucedemo.com/")

    title=page.locator(".login_logo")

    expect(title).to_be_visible()
    print(title.inner_text())