import Autotest_appium
import login
import search_audio
import edit_name_audio
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

def delete_audio(driver):
    # time.sleep(5)

    # Tìm phần tử ghi chú
    delete_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Xoá"))
    )
    # delete_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Xoá")
    delete_button.click()
    time.sleep(3)
  
    # Nhấn phím lưu trên bàn phím Android
    confirm_delete_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Xoá")
    confirm_delete_button.click()
    time.sleep(5)

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)

    search_text = "ghi chu"
    search_audio.search_audio(driver, wait, search_text)
    edit_name_audio.swipe_audio(driver)     
    delete_audio(driver)
