from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def setup_driver():
    # Tạo đối tượng options cho Android
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "AHB00009462")
    options.set_capability("appPackage", "vn.vais.memobot")
    options.set_capability("appActivity", "com.ryanheise.audioservice.AudioServiceActivity")
    options.set_capability("noReset", True)
    options.set_capability("fullReset", False)  
    options.set_capability("appWaitForLaunch", True)    
    options.set_capability("dontStopAppOnReset", True)
    options.set_capability("autoGrantPermissions", True)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # Đợi một chút để app mở
    time.sleep(5)

    print("✅ Mở app thành công!")
    return driver