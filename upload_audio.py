import Autotest_appium
import login
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey

import time

def upload_file(driver, file_path):
    main_button = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    main_button.click()
    time.sleep(3)

    upload_button = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Tải lên\nfile']")
    upload_button.click()
    time.sleep(3)

    choose_file_button = driver.find_element(
        AppiumBy.XPATH,
        "//android.widget.ImageView[@content-desc='Chọn file tải lên']"
    )
    choose_file_button.click()
    time.sleep(5)
    print(driver.page_source)


    # file_input = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    # file_input.send_keys("/sdcard/Download/test-audio.mp3")
    # time.sleep(3)
    # Click vào file cụ thể "REC_230627_105611.m4a"


    # # 2. Chọn folder "Audio"
    # audio_folder = driver.find_element(
    #     AppiumBy.XPATH,
    #     "//android.widget.TextView[@text='Audio']"
    # )
    # audio_folder.click()
    # time.sleep(2)

    # # 3. Chọn folder "Unknown"
    # sound_folder = driver.find_element(
    #     AppiumBy.XPATH,
    #     "//android.widget.TextView[@text='Unknown']"
    # )

    # # 4. Chọn folder "SoundRecorder"
    # sound_folder = driver.find_element(
    #     AppiumBy.XPATH,
    #     "//android.widget.TextView[@text='SoundRecorder']"
    # )
    # sound_folder.click()
    # time.sleep(2)

    # 4. Chọn file "REC_230627_105611.m4a"
    target_file = driver.find_element(
        AppiumBy.XPATH,
        "//android.widget.TextView[@text='REC_230627_105611.m4a']"
    )
    target_file.click()
    time.sleep(5)



    # Lấy toàn bộ XML của màn hình hiện tại
    xml_source = driver.page_source

    # Kiểm tra đoạn text có xuất hiện không
    if "REC_230627_105611" in xml_source:
        print("✅ Audio từ thiết bị đã được upload!")
    else:
        print("❌ Audio từ thiết bị đã upload không thành công!")

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)
    
    file_path = "path/to/your/audio/file.mp3"  # Replace with your actual file path
    upload_file(driver, file_path)
