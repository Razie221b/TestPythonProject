import pytest
from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers
from pytest_bdd import scenarios

from configs.configDataProvider import baseURL

scenarios('../features/LearnMode.feature')


def is_not_null(value: str) -> bool:
    return value is not None and value.strip().lower() != 'null' and value.strip() != ""


@given(parsers.parse('I am on the adder page'))
def navigate_to_adder(page):
    if page.url != "https://bugeater.web.app/app/challenge/learn/adder":
        page.goto(baseURL)
        page.get_by_role("button", name="Accept").click()
        expect(page.get_by_text("We use cookies to improve your experience")).not_to_be_visible()
        page.locator('[href="/app/challenge/learn/adder"]').click()
        page.get_by_role("button", name="skip").click()


@when(parsers.parse('I enter "{num1}" and "{num2}" into the input fields'))
def check_title(page, num1, num2):
    if is_not_null(num1):
        page.get_by_test_id("input_1").fill(num1)
    if is_not_null(num2):
        page.get_by_test_id("input_2").fill(num2)
    page.get_by_test_id("submit").click()
    page.wait_for_timeout(1000)


@then(parsers.parse('I should see the result "{result}"'))
def verify_expected_result3(page, result):
    expect(page.get_by_test_id("result")).to_have_text(f"Result: {result}")


@given(parsers.parse('I am on the divider page'))
def navigate_to_divider(page):
    if page.url != "https://bugeater.web.app/app/challenge/learn/divider":
        page.goto(baseURL)
        page.locator('[href="/app/challenge/learn/divider"]').click()
