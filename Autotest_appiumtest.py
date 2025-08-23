from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey

import time

# Tạo đối tượng options cho Android
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "AHB00009462")
options.set_capability("appPackage", "vn.vais.memobot")
options.set_capability("appActivity", "com.ryanheise.audioservice.AudioServiceActivity")

# Khởi tạo session
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Đợi một chút để app mở
time.sleep(5)

print("✅ Mở app thành công!")

# 👉 Click vào nút "Tiếng Việt"
radio_vietnamese = driver.find_element(By.ACCESSIBILITY_ID, "Tiếng Việt")
radio_vietnamese.click()
print("✅ Click nút Tiếng Việt")

time.sleep(1)

btn_confirm = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Xác nhận']"))
)
btn_confirm.click()
time.sleep(5)

fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
username_field = fields[0]
password_field = fields[1]

username_field.click()
username_field.send_keys("memo15@mailinator.com")
time.sleep(1)

password_field.click()
password_field.send_keys("Abcd@123456")
time.sleep(3)

driver.hide_keyboard()
time.sleep(3)
login_button = driver.find_element(AppiumBy.XPATH,
    '(//android.view.View[@content-desc="Đăng nhập"])[2]')
login_button.click()
time.sleep(5)

print("✅ Đăng nhập thành công!")

# Tìm element theo content-desc
search_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tìm kiếm nội dung")

# Click vào ô tìm kiếm
search_field.click()
time.sleep(2)

# Tìm element EditText (giả sử chỉ có 1)
edit_text = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")

# Click vào ô EditText
edit_text.click()
time.sleep(1)

# Gửi text vào EditText
edit_text.send_keys("ghi chu")
# Nhấn phím Enter trên bàn phím Android
driver.press_keycode(AndroidKey.ENTER)
time.sleep(5)

print("✅ Tìm kiếm thành công!")

