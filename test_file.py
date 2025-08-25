import Autotest_appium
import login
from selenium.webdriver.support.ui import WebDriverWait

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
