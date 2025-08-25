import Autotest_appium
from appium import webdriver
import login
import chat_AI
import search_audio
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time

def go_to_share_audio(driver):
    home_tab = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.ImageView[contains(@content-desc, 'Trang chủ')]"
    )
    home_tab.click()
    time.sleep(3)

    search_audio.search_audio(driver, wait, "Vincom")
    chosen_audio = driver.find_element(
    AppiumBy.XPATH,
    "//android.view.View[contains(@content-desc, 'Vincom')]"
    )
    chosen_audio.click()
    time.sleep(10)

def set_up_share_audio(driver):
    go_to_share_audio(driver)
    setup_share_button = "[912,118][1056,262]"
    chat_AI.click_element_by_bounds(driver, setup_share_button)
    time.sleep(3)

    shared_file_radio_btn = driver.find_element(
        AppiumBy.XPATH, "//android.view.View[@content-desc='Chia sẻ cả file ghi âm']/android.widget.RadioButton"
    )
    # Click vào nút
    shared_file_radio_btn.click()
    time.sleep(3)
    shared_button = driver.find_element(
        AppiumBy.XPATH, "(//android.view.View[@content-desc='Chia sẻ'])[2]"
    )
    shared_button.click()
    time.sleep(5)
    print("Đã mở dropdown option chia sẻ file ghi âm")

    # Tìm các option trong "Cho phép người khác xem đoạn text tóm tắt"

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    email_user = "memo1@mailinator.com"
    password_user = "Abcd@12345"
    # login.login(driver, wait, email_pro, password_pro)
    set_up_share_audio(driver)
    


