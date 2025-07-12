import pytest
import configparser

from typing import Any, Generator
from playwright.sync_api import sync_playwright, Browser, Page, expect
from framework.playwright_manager import PlaywrightManager
from configs.configDataProvider import is_headless, browser_name, width, height, ignoreHttpsErrors, baseURL
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


def pytest_sessionfinish(session, exitstatus):
    log.info("pytest_sessionfinish triggered. Forcing cleanup...")

    try:
        if PlaywrightManager.page:
            PlaywrightManager.page.close()
            log.info("Page closed.")
    except Exception as e:
        log.warning(f"Error closing page: {e}")

    try:
        if PlaywrightManager.browser:
            PlaywrightManager.browser.close()
            log.info("Browser closed.")
    except Exception as e:
        log.warning(f"Error closing browser: {e}")

    try:
        if PlaywrightManager.playwright:
            PlaywrightManager.playwright.stop()
            log.info("Playwright stopped.")
    except Exception as e:
        log.warning(f"Error stopping Playwright: {e}")
