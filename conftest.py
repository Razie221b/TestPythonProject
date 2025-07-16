import pytest
import configparser

from typing import Any, Generator
from playwright.sync_api import sync_playwright, Browser, Page
from framework.playwright_manager import PlaywrightManager
from configs.configDataProvider import is_headless, browser_name, width, height, ignoreHttpsErrors
from helper import log


@pytest.fixture(scope="session")
def get_config():
    config = configparser.ConfigParser()
    config.read('configs.ini')
    return config


@pytest.fixture(scope="session")
def browser(get_config) -> Generator[Browser, Any, None]:
    log.info(f"Setting up browser: {browser_name}, Headless: {is_headless}")

    PlaywrightManager.playwright = sync_playwright().start()
    pw = PlaywrightManager.playwright

    if browser_name.lower() == 'chromium':
        browser_instance = pw.chromium.launch(headless=is_headless)
    elif browser_name.lower() == 'firefox':
        browser_instance = pw.firefox.launch(headless=is_headless)
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    PlaywrightManager.browser = browser_instance
    yield browser_instance

    log.info("Closing browser and Playwright...")
    browser_instance.close()
    pw.stop()
    log.info("Teardown complete.")


@pytest.fixture(scope="session")
def page(browser: Browser) -> Generator[Page, Any, None]:
    log.info("Creating a new page for the test.")
    context = browser.new_context()
    new_page = context.new_page()
    PlaywrightManager.page = new_page

    yield new_page

    log.info("Closing page and context...")
    new_page.close()
    context.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": ignoreHttpsErrors,
        "viewport": {
            "width": width,
            "height": height,
        }
    }


def pytest_runtest_setup(item):
    if "active1" not in item.keywords:
        pytest.skip("Skipped because test does not have @active tag.")
