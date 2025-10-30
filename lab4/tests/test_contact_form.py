from pathlib import Path
from lab4.pages.contact_page import ContactPage


def test_submit_contact_form_success(driver):
    page = ContactPage(driver)
    page.open_local()

    page.fill_form(name="Alice Smith", email="alice@example.com", message="Hello!")
    page.submit()

    assert page.success_visible(), "Success message should be visible after valid submission"


def test_submit_contact_form_missing_name_shows_error(driver):
    page = ContactPage(driver)
    page.open_local()

    page.fill_form(name="", email="alice@example.com", message="Hello!")
    page.submit()

    assert page.error_name_visible(), "Name error should be visible for empty name"
    assert not page.success_visible(), "Success message must not be shown on invalid submission"
