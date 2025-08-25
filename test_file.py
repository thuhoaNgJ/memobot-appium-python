import Autotest_appium
import login
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey

import time

def function():
    pass

if __name__ == "__main__":
    # khởi tạo driver và đăng nhập
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)
    # gọi hàm 
    function()
