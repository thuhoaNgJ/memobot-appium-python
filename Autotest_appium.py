from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey

import time

def setup_driver():
    # Tạo đối tượng options cho Android
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "AHB00009462")
    options.set_capability("appPackage", "vn.vais.memobot")
    options.set_capability("appActivity", "com.ryanheise.audioservice.AudioServiceActivity")

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # Đợi một chút để app mở
    time.sleep(5)

    print("✅ Mở app thành công!")
    return driver