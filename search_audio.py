import Autotest_appium
import login
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time

def search_audio(driver, wait, search_text):
    # Tìm element theo content-desc
    search_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tìm kiếm nội dung")

    # Click vào ô tìm kiếm
    search_field.click()
    time.sleep(2)

    # Tìm element EditText (giả sử chỉ có 1)
    edit_text = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")

    # Click vào ô EditText
    edit_text.click()
    time.sleep(1)

    # Gửi text vào EditText
    edit_text.send_keys(search_text)
    # Nhấn phím Enter trên bàn phím Android
    driver.press_keycode(AndroidKey.ENTER)
    time.sleep(5)

    print("✅ Tìm kiếm thành công!")

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)

    search_text = "ghi chu"
    search_audio(driver, wait, search_text)
