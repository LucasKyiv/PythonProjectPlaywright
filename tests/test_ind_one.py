import re
import time

from playwright.sync_api import expect, Page


def test_google_search(page: Page):
    page.goto('https://www.google.com/ncr')
    try:
        # Try to click the cookie consent button
        page.locator("button:has-text('Accept')").click(timeout=5000)
    except Exception as e:
        print("Cookie banner not found, capturing debug info...")
        page.screenshot(path="debug_screenshot.png", full_page=True)
        with open("debug_page.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        raise e  # rethrow so CI fails (and you can inspect the logs)
    page.locator("button:has-text('Accept')").click()
    page.get_by_role("combobox").fill("OpenAI")
    time.sleep(2)
    page.keyboard.press("Escape")
    page.screenshot(path="before_click.png")
    page.get_by_role("button", name="Google Search").click(timeout=5000)
    expect(page).to_have_title(re.compile("OpenAI", re.IGNORECASE))
