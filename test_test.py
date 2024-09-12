import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(scope="module")
def playwright():
    with sync_playwright() as p:
        yield p

def test_playwright_trace(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=2000)  # Ensure headless mode
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    context.tracing.stop(path="traces/trace.zip")
    context.close()
    browser.close()
