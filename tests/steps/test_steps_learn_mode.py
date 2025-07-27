from pytest_bdd import given, when, then, parsers
from pytest_bdd import scenarios
from configs.configDataProvider import *
from tests.steps.page_actions import *
from helper import *

scenarios('../tests/features/Bugeater.feature')


@given(parsers.parse('I am on the "{page_title}" page'))
def navigate_to_page(page, page_title: str):
    valid_urls = [
        numberAdditionURL,
        numberDivisionURL,
        passwordRestoreURL,
        updateProfileURL
    ]

    if page.url not in valid_urls:
        page.goto(listURL)
        page.wait_for_timeout(1000)
        click_accept_button(page)
        match page_title:
            case "number addition":
                page.locator('[href="/app/challenge/learn/adder"]').click()

            case "number division":
                page.locator('[href="/app/challenge/learn/divider"]').click()

            case "password restore":
                page.locator('[href="/app/challenge/learn/passwordRestore"]').click()

            case "update nickname":
                page.locator('[href="/app/challenge/learn/updateNickname"]').click()

            case _:
                raise ValueError(f"Navigation logic for '{page_title}' is not defined.")

        click_skip_button(page)


@when(parsers.parse('I enter "{num1}" and "{num2}" into the input fields'))
def enter_num1_and_num2(page, num1, num2):
    if is_not_null(num1):
        fill_input_field(page, "input_1", num1)
    if is_not_null(num2):
        fill_input_field(page, "input_2", num2)
    click_submit_button(page)
    page.wait_for_timeout(1000)


@when(parsers.parse('I enter "{new_password}" into the input field'))
def enter_new_password(page, new_password):
    if is_not_null(new_password):
        fill_input_field(page, "input_1", new_password)
    click_submit_button(page)
    page.wait_for_timeout(1000)


@when(parsers.parse('I enter "{nick_name}" and "{first_name}" and "{last_name}" into the input field'))
def enter_nick_name_and_first_name_and_last_name(page, nick_name, first_name, last_name):
    if is_not_null(nick_name):
        fill_input_field(page, "input_1", nick_name)
    if is_not_null(first_name):
        fill_input_field(page, "input_2", first_name)
    if is_not_null(last_name):
        fill_input_field(page, "input_3", last_name)

    click_submit_button(page)
    page.wait_for_timeout(1000)


@when(parsers.parse('I enter "{nick_name}" and "{first_name}" and "{last_name}" into the input fields'))
def enter_nick_name_and_first_name_and_last_name(page, nick_name, first_name, last_name):
    if is_not_null(nick_name):
        fill_input_field(page, "input_1", nick_name)
    if is_not_null(first_name):
        fill_input_field(page, "input_2", first_name)
    if is_not_null(last_name):
        fill_input_field(page, "input_3", last_name)

    click_submit_button(page)
    page.wait_for_timeout(1000)


@then(parsers.parse('I should see the result "{result}"'))
def verify_expected_result(page, result):
    expect(page.get_by_test_id("result")).to_have_text(f"Result: {result}")
