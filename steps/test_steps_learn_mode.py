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
        accept_button = page.get_by_role("button", name="Accept")
        skip_button = page.get_by_role("button", name="skip")

        page.wait_for_timeout(1000)
        if expect(accept_button).to_be_visible():
            accept_button.click()
            expect(page.get_by_text("We use cookies to improve your experience")).not_to_be_visible()

        page.locator('[href="/app/challenge/learn/adder"]').click()
        if expect(skip_button).to_be_visible():
            skip_button.click()


@given(parsers.parse('I am on the divider page'))
def navigate_to_divider(page):
    if page.url != "https://bugeater.web.app/app/challenge/learn/divider":
        page.goto(baseURL)
        accept_button = page.get_by_role("button", name="Accept")
        skip_button = page.get_by_role("button", name="skip")

        page.wait_for_timeout(1000)
        if expect(accept_button).to_be_visible():
            accept_button.click()
            expect(page.get_by_text("We use cookies to improve your experience")).not_to_be_visible()

        page.locator('[href="/app/challenge/learn/divider"]').click()
        if expect(skip_button).to_be_visible():
            skip_button.click()


@given(parsers.parse('I am on the password restore page'))
def navigate_to_password_restore(page):
    if page.url != "https://bugeater.web.app/app/challenge/learn/passwordRestore":
        page.goto(baseURL)
        accept_button = page.get_by_role("button", name="Accept")
        skip_button = page.get_by_role("button", name="skip")
        page.wait_for_timeout(1000)

        if accept_button.is_visible():
            accept_button.click()
            expect(page.get_by_text("We use cookies to improve your experience")).not_to_be_visible()

        page.locator('[href="/app/challenge/learn/passwordRestore"]').click()
        if skip_button.is_visible():
            skip_button.click()


@when(parsers.parse('I enter "{num1}" and "{num2}" into the input fields'))
def enter_num1_and_num2(page, num1, num2):
    if is_not_null(num1):
        page.get_by_test_id("input_1").fill(num1)
    if is_not_null(num2):
        page.get_by_test_id("input_2").fill(num2)
    page.get_by_test_id("submit").click()
    page.wait_for_timeout(1000)


@when(parsers.parse('I enter "{new_password}" into the input field'))
def enter_new_password(page, new_password):
    if is_not_null(new_password):
        page.get_by_test_id("input_1").fill(new_password)
    page.get_by_test_id("submit").click()
    page.wait_for_timeout(1000)


@then(parsers.parse('I should see the result "{result}"'))
def verify_expected_result(page, result):
    expect(page.get_by_test_id("result")).to_have_text(f"Result: {result}")
