import re
import time

from playwright.sync_api import expect, Page


def test_google_search(page: Page):
    page.goto('https://www.google.com/ncr')
    page.get_by_role("combobox").fill("OpenAI")
    time.sleep(2)
    page.keyboard.press("Escape")
    page.screenshot(path="before_click.png")
    page.get_by_role("button", name="Google Search").click(timeout=5000)
    expect(page).to_have_title(re.compile("OpenAI", re.IGNORECASE))
