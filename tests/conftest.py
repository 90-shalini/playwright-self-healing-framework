import pytest

from playwright.sync_api import sync_playwright, expect
from utils.screenshot import capture_screenshot


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        yield page

        browser.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        print("COMING HERE!!")
        page = item.funcargs.get("page")

        if page:
            capture_screenshot(
                page,
                item.name
            )
        