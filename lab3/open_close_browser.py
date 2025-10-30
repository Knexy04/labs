import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


URL = os.getenv("URL", "https://www.saucedemo.com/")


def build_driver():
    browser = os.getenv("BROWSER", "chrome").strip().lower()
    headless = os.getenv("HEADLESS", "0").strip() in {"1", "true", "yes"}

    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def main():
    driver = build_driver()
    try:
        driver.get(URL)
        print("Page title:", driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
