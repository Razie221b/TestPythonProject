from playwright.sync_api import expect
from pytest_bdd import given, when, then
from configs.configDataProvider import baseURL
from pytest_bdd import scenarios

scenarios('../features/NumberAddition.feature')


@given('open base URL')
def open_base_url(page):
    page.goto(baseURL)
    page.get_by_role("button", name="Accept").click()
    expect(page.get_by_text("We use cookies to improve your experience")).not_to_be_visible()


@when('enter "1" and "2" into the input fields')
def check_title(page):
    page.locator('[href="/app/challenge/learn/adder"]').click()
    page.get_by_role("button", name="skip").click()
    page.get_by_test_id("input_1").fill("1")
    page.get_by_test_id("input_2").fill("2")
    page.get_by_test_id("submit").click()


@then('verify expected result: "3"')
def verify_expected_result3(page):
    expect(page.get_by_test_id("result")).to_have_text("Result: 3")
