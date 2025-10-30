from pathlib import Path
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        if url.startswith("file://") or url.startswith("http"):
            self.driver.get(url)
            return
        # Allow passing a relative filesystem path
        path = Path(url).resolve().as_uri()
        self.driver.get(path)

    def find(self, locator: Locator):
        return self.driver.find_element(*locator)

    def click(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator: Locator, text: str) -> None:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def text_of(self, locator: Locator) -> str:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text.strip()
