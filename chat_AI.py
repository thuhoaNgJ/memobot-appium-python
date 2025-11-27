import Autotest_appium
import login
import search_audio
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time

# tính toạ độ của textbox chat AI để tap vào
def get_center_from_bounds(bounds: str):
    # bounds dạng "[48,1689][1011,1872]"
    bounds = bounds.replace("[", "").replace("]", ",")
    nums = [int(x) for x in bounds.split(",") if x.strip() != ""]
    x1, y1, x2, y2 = nums
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    return x, y

def click_element_by_bounds(driver, bounds):
    x, y = get_center_from_bounds(bounds)
    print(x, y)  # 529 1780

    # tạo "ngón tay"
    finger = PointerInput("touch", "finger")   # ✅ dùng "touch" thay vì PointerInput.TOUCH
    actions = ActionBuilder(driver, mouse=finger)

    # tap
    actions.pointer_action.move_to_location(x, y)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pointer_up()
    actions.perform()

def chat_AI(driver, bounds):
    time.sleep(5)
    chosen_audio = driver.find_element(
    AppiumBy.XPATH,
    "//android.view.View[contains(@content-desc, 'Vincom')]"
    )
    chosen_audio.click()
    # time.sleep(5)
    chatAI_screen_button = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH,
        "//android.view.View[@content-desc='Chat với AI']"
    )))
    # chatAI_screen_button = driver.find_element(
    #     AppiumBy.XPATH,
    #     "//android.view.View[@content-desc='Chat với AI']"
    # )
    chatAI_screen_button.click()
    time.sleep(10)

    click_element_by_bounds(driver, bounds)

    # sau đó gõ text
    driver.execute_script("mobile: type", {"text": "Câu hỏi Hoạt động kinh doanh năm 2023 của Vincom"})
    driver.press_keycode(AndroidKey.ENTER)
    
if __name__ == "__main__":
    driver = Autotest_appium.setup_driver()
    wait = WebDriverWait(driver, 10)
    email_pro= "memo15@mailinator.com"
    password_pro = "Abcd@123456"
    login.login(driver, wait, email_pro, password_pro)

    search_text = "Vincom"
    search_audio.search_audio(driver, wait, search_text)
    bounds = "[48,1689][1011,1872]"
    chat_AI(driver, bounds)