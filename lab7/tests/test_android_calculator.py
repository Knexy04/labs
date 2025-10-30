import os
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.mark.android
def test_launches_target_app(android_driver):
    target_pkg = os.getenv("APP_PACKAGE", "com.android.calculator2")

    # Assert session is alive and app is in foreground
    assert android_driver.session_id
    assert android_driver.current_package == target_pkg

    # Optional best-effort functional check for stock Calculator
    try:
        two = android_driver.find_element(By.ID, f"{target_pkg}:id/digit_2")
        plus = android_driver.find_element(By.ACCESSIBILITY_ID, "plus")
        three = android_driver.find_element(By.ID, f"{target_pkg}:id/digit_3")
        equals = android_driver.find_element(By.ACCESSIBILITY_ID, "equals")
        two.click(); plus.click(); three.click(); equals.click()
        # Result field ids differ, so we don't hard assert on value
    except NoSuchElementException:
        # Device-specific calculator variants may not match selectors — acceptable for smoke
        pass
