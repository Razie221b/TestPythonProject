from pytest_bdd import scenario, given, then
from playwright.sync_api import Page
import logging

log = logging.getLogger()


@scenario('../features/login.feature', 'Visit Google homepage')
def test_login():
    pass


@given('I am on the Google homepage')
def navigate_to_google(page: Page):
    log.info("Navigating to Google homepage...")
    page.goto("https://www.google.com")


@then('I should see the title "Google"')
def check_title(page: Page):
    log.info("Verifying page title...")
    assert "Google" in page.title()
    log.info("Title verified successfully.")
