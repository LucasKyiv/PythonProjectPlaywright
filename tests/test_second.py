
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://coffee-cart.app/"

@pytest.fixture(scope="function")
def open_app(page: Page):
    page.goto(BASE_URL)
    return page


def test_page_loads(open_app):
    expect(open_app.locator("h1")).to_have_text("Payment details")


def test_add_item_to_cart(open_app):
    page = open_app
    espresso = page.locator('[data-test="Espresso"]')
    espresso.click()
    cart_item = page.locator('[href="/cart"]')
    expect(cart_item).to_be_visible()

