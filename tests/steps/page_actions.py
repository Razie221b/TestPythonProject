from playwright.sync_api import expect


def click_accept_button(page):
    accept_button = page.get_by_role("button", name="Accept")
    if accept_button.is_visible():
        accept_button.click()
        expect(page.get_by_text("We use cookies to improve your experience")).not_to_be_visible()


def click_skip_button(page):
    skip_button = page.get_by_role("button", name="skip")
    if skip_button.is_visible():
        skip_button.click()


def fill_input_field(page, input_name, value):
    page.get_by_test_id(input_name).fill(value)


def click_submit_button(page):
    page.get_by_test_id("submit").click()