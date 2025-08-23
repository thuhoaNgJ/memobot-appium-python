import Autotest_appium
import login
import search_audio
import chat_AI

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time

def input_text_in_edit_text(driver):
    time.sleep(5)
    chosen_audio = driver.find_element(
    AppiumBy.XPATH,
    "//android.view.View[contains(@content-desc, 'Vincom')]"
    )
    chosen_audio.click()
    time.sleep(10)

    bounds1 = "[916,742][988,814]" #nút sửa
    chat_AI.click_element_by_bounds(driver, bounds1)
    time.sleep(5)
    print("Đã click vào nút sửa")

    # sau đó gõ text
    bounds2 = "[176,1217][864,1268]" #1 đoạn text ở tóm tắt
    chat_AI.click_element_by_bounds(driver, bounds2)
    driver.execute_script("mobile: type", {"text": ". Đây là đoạn text được thêm. "})
    # driver.press_keycode(AndroidKey.ENTER)
    time.sleep(5)

    bounds3 = "[[915,387][988,441]" #nút lưu
    chat_AI.click_element_by_bounds(driver, bounds3)

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)

    search_text = "Vincom"
    search_audio.search_audio(driver, wait, search_text)

    input_text_in_edit_text(driver)