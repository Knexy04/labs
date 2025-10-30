import os
import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def android_driver():
    appium_url = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")

    # Defaults target the stock Android Calculator app on AOSP-like systems
    caps = {
        "platformName": os.getenv("PLATFORM_NAME", "Android"),
        "appium:automationName": os.getenv("AUTOMATION_NAME", "UiAutomator2"),
        "appium:deviceName": os.getenv("DEVICE_NAME", "Android Emulator"),
        "appium:platformVersion": os.getenv("PLATFORM_VERSION", ""),
        "appium:noReset": True,
        "appium:newCommandTimeout": 120,
        "appium:appPackage": os.getenv("APP_PACKAGE", "com.android.calculator2"),
        "appium:appActivity": os.getenv("APP_ACTIVITY", ".Calculator"),
    }

    driver = webdriver.Remote(appium_url, caps)
    yield driver
    driver.quit()
