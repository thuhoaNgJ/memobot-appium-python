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
    setup_share_button = "[912,118][1056,262]"
    setup_share_button.click_element_by_bounds(driver, setup_share_button)
    time.sleep(5)
    print("Đã click vào nút chia sẻ")

    # Tìm nút radio trong "Chia sẻ cả file ghi âm"
    radio_btn = driver.find_element(
        AppiumBy.XPATH, "//android.view.View[@content-desc='Chia sẻ cả file ghi âm']/android.widget.RadioButton"
    )

    # Click vào nút
    radio_btn.click()

    print("✅ Đã click vào nút 'Chia sẻ cả file ghi âm'")   
    time.sleep(5)
    


    bounds2 = "[176,1217][864,1268]" #1 đoạn text ở tóm tắt
    chat_AI.click_element_by_bounds(driver, bounds2)
    driver.execute_script("mobile: type", {"text": ". Đây là đoạn text được thêm."})
    time.sleep(5)

    bounds3 = "[[915,387][988,441]" #nút lưu
    chat_AI.click_element_by_bounds(driver, bounds3)

def check_not_allow_see_audio(driver):
    login.login(driver, wait, email_pro, password_pro)



    return

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    email_user = "memo1@mailinator.com"
    password_user = "Abcd@12345"
    


