
import Autotest_appium
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, wait, email, password):
    # Click on "Tiếng Việt"
    # use AppiumBy with explicit wait instead of By.ACCESSIBILITY_ID
    radio_vietnamese = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Tiếng Việt"))
    )
    radio_vietnamese.click()
    print("✅ Click nút Tiếng Việt")

    # time.sleep(1)

    btn_confirm = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Xác nhận']"))
    )
    btn_confirm.click()
    time.sleep(5)

    # wait for button username and password to be present
    field_button = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
    )
    if len(field_button) < 2:
        raise RuntimeError("Expected at least 2 EditText fields for username and password")

    username_field = field_button[0]
    password_field = field_button[1]

    username_field.click()
    username_field.send_keys(email)
    time.sleep(1)

    password_field.click()
    password_field.send_keys(password)
    time.sleep(1)

    # hide keyboard safely
    try:
        driver.hide_keyboard()
    except Exception:
        pass
    time.sleep(1)
    
    login_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.View[@content-desc="Đăng nhập"])[2]'))
    )
    login_button.click()
    time.sleep(5)

    print("✅ Đăng nhập thành công!")

def logout(driver, email):
    # use explicit wait here too
    wait = WebDriverWait(driver, 10)
    account_tab = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc, 'Tài khoản')]"))
    )
    account_tab.click()
    # time.sleep(2)

    account = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, f"//android.view.View[contains(@content-desc, '{email}')]"))
    )
    account.click()
    # time.sleep(1)

    logout_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@content-desc='Thoát tài khoản']"))
    )
    logout_button.click()
    # time.sleep(1)

    confirm_logout_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.View[@content-desc='Xác nhận']"))
    )
    confirm_logout_button.click()
    time.sleep(2)

    print("✅ Đăng xuất thành công!")

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login(driver, wait, email_pro, password_pro)
    logout(driver, email_pro)