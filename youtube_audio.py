import Autotest_appium
import login
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time

def transcribe_youtube(driver, youtube_link):
    main_button = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    main_button.click()
    time.sleep(3)

    link_youtube_button = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Link\nYoutube"]')
    link_youtube_button.click()
    time.sleep(3)

    # Tìm phần tử theo class name (giả sử chỉ có 1 EditText)
    edit_text = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")

    # Click vào ô nhập
    edit_text.click()
    time.sleep(1)

    # Gửi nội dung vào ô nhập
    edit_text.send_keys(youtube_link)
    time.sleep(3)
    # Nhấn phím Enter trên bàn phím Android
    # Tìm và click vào button "Bắt đầu"
    start_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Bắt đầu")
    start_button.click()
    
    time.sleep(10)  
    # Lấy toàn bộ XML của màn hình hiện tại
    xml_source = driver.page_source

    # Kiểm tra đoạn text có xuất hiện không
    if "https://youtu.be/" in xml_source:
        print("✅ Audio link youtube đã được upload!")
    else:
        print("❌ Audio link youtube đã được upload không thành công!")

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)

    youtube_link = "https://youtu.be/wO8LTo0PsTg?si=vfG-S_w8EFvGaQsX"
    transcribe_youtube(driver, youtube_link)  
