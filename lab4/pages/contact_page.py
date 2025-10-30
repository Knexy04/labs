from pathlib import Path
from typing import Optional
from selenium.webdriver.common.by import By
from .base_page import BasePage, Locator


class ContactPage(BasePage):
    NAME: Locator = (By.ID, "name")
    EMAIL: Locator = (By.ID, "email")
    MESSAGE: Locator = (By.ID, "message")
    SUBMIT: Locator = (By.ID, "submit-btn")

    ERROR_NAME: Locator = (By.ID, "error-name")
    ERROR_EMAIL: Locator = (By.ID, "error-email")
    ERROR_MESSAGE: Locator = (By.ID, "error-message")
    SUCCESS_MESSAGE: Locator = (By.ID, "success-message")

    def open_local(self, file_path: Optional[str] = None) -> None:
        if file_path is None:
            file_path = str(Path(__file__).resolve().parent.parent / "site" / "contact.html")
        self.open(file_path)

    def fill_form(self, name: str, email: str, message: str) -> None:
        self.type(self.NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.MESSAGE, message)

    def submit(self) -> None:
        self.click(self.SUBMIT)

    def success_visible(self) -> bool:
        return self.is_visible(self.SUCCESS_MESSAGE)

    def error_name_visible(self) -> bool:
        return self.is_visible(self.ERROR_NAME)

    def error_email_visible(self) -> bool:
        return self.is_visible(self.ERROR_EMAIL)

    def error_message_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
