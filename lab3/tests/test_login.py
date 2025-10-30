from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")

    username = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.clear()
    username.send_keys("standard_user")
    password.clear()
    password.send_keys("secret_sauce")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    # Дополнительная проверка: наличие элемента корзины после входа
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "shopping_cart_container"))
    )

    assert "inventory" in driver.current_url
