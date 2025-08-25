import Autotest_appium
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, wait, email, password):
    # Click on "Tiếng Việt"
    radio_vietnamese = driver.find_element(By.ACCESSIBILITY_ID, "Tiếng Việt")
    radio_vietnamese.click()
    print("✅ Click nút Tiếng Việt")

    time.sleep(1)

    btn_confirm = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Xác nhận']"))
    )
    btn_confirm.click()
    time.sleep(5)

    fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    username_field = fields[0]
    password_field = fields[1]

    username_field.click()
    username_field.send_keys(email)
    time.sleep(1)

    password_field.click()
    password_field.send_keys(password)
    time.sleep(3)

    driver.hide_keyboard()
    time.sleep(3)
    
    login_button = driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="Đăng nhập"])[2]')
    login_button.click()
    time.sleep(5)

    print("✅ Đăng nhập thành công!")


def logout(driver, email):
    account_tab = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.ImageView[contains(@content-desc, 'Tài khoản')]"
    )
    account_tab.click()
    time.sleep(5)

    account = driver.find_element(
        AppiumBy.XPATH, f"//android.view.View[contains(@content-desc, '{email}')]"
    )
    account.click()

    # Click on "Logout" button
    logout_button = driver.find_element(
        AppiumBy.XPATH, f"//android.view.View[@content-desc='Thoát tài khoản']"
    )
    logout_button.click()
    time.sleep(3)

    confirm_logout_button = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Xác nhận']")
    confirm_logout_button.click()
    time.sleep(3)

    print("✅ Đăng xuất thành công!")


if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login(driver, wait, email_pro, password_pro)
    logout(driver, email_pro)

