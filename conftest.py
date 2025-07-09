from typing import Any, Generator

import pytest
import configparser
from playwright.sync_api import Playwright, sync_playwright, Browser, Page
from framework.playwright_manager import PlaywrightManager
import logging
from config.configDataProvider import is_headless
from config.configDataProvider import browser_name

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


@pytest.fixture(scope="session")
def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
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


@pytest.fixture
def page(browser: Browser) -> Generator[Page, Any, None]:
    log.info("Creating a new page for the test.")
    context = browser.new_context()
    new_page = context.new_page()
    PlaywrightManager.page = new_page

    yield new_page

    log.info("Closing page and context...")
    new_page.close()
    context.close()
