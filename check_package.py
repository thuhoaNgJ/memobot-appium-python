import Autotest_appium
import login
import youtube_audio
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

import time

def go_to_package_screen(driver):
    upgrade_tab = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.ImageView[contains(@content-desc, 'Nâng cấp')]"
    )
    upgrade_tab.click()
    time.sleep(5)
    
    goi_hien_tai_element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH,
                                       '//android.view.View[@content-desc="Gói hiện tại"]'))
    )
    # goi_hien_tai_element = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Gói hiện tại"]')
    goi_hien_tai_element.click()

def get_present_package_infor(driver):
    # Lấy tất cả các element là android.view.View
    elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")

    # Biến kết quả
    used_files = None
    used_minutes = None
    used_hours = None

    for el in elements:
        desc = el.get_attribute("content-desc")
        # Kiểm tra xem có thuộc tính content-desc không va co chua "tệp", "phút", "giờ"
        is_checked = re.search(r"\d+ /? \d+ (tệp|phút|giờ)", desc) if desc else None
        if not desc or not is_checked:
            continue

        # Kiểm tra theo từng loại thông tin
        if re.match(r"^\d+ / \d+ tệp$", desc):
            used_files = int(desc.split(" / ")[0])
        elif re.match(r"^\d+ / \d+ phút$", desc):
            used_minutes = int(desc.split(" / ")[0])
        elif re.match(r"^\d+ / \d+ giờ$", desc):
            used_hours = int(desc.split(" / ")[0])
    # In kết quả
    return {
        "used_files": used_files,
        "used_minutes": used_minutes,
        "used_hours": used_hours
    }

def get_package_after_upload_file(driver):
    youtube_link = "https://youtu.be/wO8LTo0PsTg?si=vfG-S_w8EFvGaQsX"
    youtube_audio.transcribe_youtube(driver, youtube_link) 
    time.sleep(10)  # Đợi một chút để quá trình upload hoàn tất
    go_to_package_screen(driver)
    time.sleep(5)
    return get_present_package_infor(driver)

def compare_change_package(driver):
    initial_info = get_present_package_infor(driver)
    print("Thông tin gói ban đầu:", initial_info)

    home_tab = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.ImageView[contains(@content-desc, 'Trang chủ')]"
    )
    home_tab.click()
    time.sleep(3)

    # Upload file và kiểm tra thông tin gói sau khi upload
    updated_info = get_package_after_upload_file(driver)
    print("Thông tin gói sau khi upload:", updated_info)

    # So sánh thông tin gói trước và sau khi upload
    if (initial_info["used_files"] < updated_info["used_files"] or
        initial_info["used_minutes"] < updated_info["used_minutes"]):
        print("✅ Gói đã thay đổi sau khi upload file.")
    else:
        print("❌ Gói không thay đổi sau khi upload file.")

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)
    go_to_package_screen(driver)
    # result = get_present_package_infor(driver)
    # print("Kết quả:", result)
    # print(result["used_files"], result["used_minutes"], result["used_hours"])
    compare_change_package(driver)