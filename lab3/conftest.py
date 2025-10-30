import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    browser = os.getenv("BROWSER", "chrome").strip().lower()
    headless = os.getenv("HEADLESS", "0").strip() in {"1", "true", "yes"}

    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(2)
    yield driver
    driver.quit()
