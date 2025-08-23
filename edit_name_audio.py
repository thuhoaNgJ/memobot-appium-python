import Autotest_appium
import login
import search_audio
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

# Link document: https://pypi.org/project/Appium-Python-Client/
def swipe_audio(driver):
    time.sleep(5)
    
    # Tìm phần tử ghi chú
    chosen_audio = driver.find_element(
        AppiumBy.XPATH,
        "//android.view.View[contains(@content-desc, 'Ghi chú')]"
    )
    # In ra content-desc
    print("Content-desc:", chosen_audio.get_attribute("content-desc"))


    # Lấy tọa độ và kích thước phần tử
    location = chosen_audio.location
    size = chosen_audio.size

    # Tính toán điểm bắt đầu và kết thúc vuốt
    start_x = location['x'] + int(size['width'] * 0.9)  # Gần mép phải
    start_y = location['y'] + int(size['height'] / 2)   # Chính giữa chiều cao
    end_x = location['x'] + int(size['width'] * 0.1)    # Gần mép trái

    # Thực hiện thao tác vuốt
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.2)  # giây, có thể dùng 0.5 nếu cần mượt hơn
    actions.w3c_actions.pointer_action.move_to_location(end_x, start_y)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def edit_name(driver):
    time.sleep(5)

    # Tìm phần tử ghi chú
    rename_button = driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Đổi tên"
    )
    rename_button.click()
    time.sleep(3)
    # Tìm tất cả các EditText trên màn hình
    edit_fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")

    # Giả sử chỉ có 1 ô input cần đổi tên → chọn phần tử đầu tiên
    edit_field = edit_fields[0]
    edit_field.click()
    edit_field.clear()
    edit_field.send_keys("Ghi chú của hoa - edited")
    time.sleep(3)
    # Nhấn phím lưu trên bàn phím Android
    save_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lưu")
    save_button.click()
    time.sleep(5)

if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)

    search_text = "ghi chu"
    search_audio.search_audio(driver, wait, search_text)
    swipe_audio(driver)     
    edit_name(driver)
