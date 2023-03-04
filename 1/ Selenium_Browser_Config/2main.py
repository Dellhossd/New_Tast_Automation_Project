from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def Webelememt_State():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    username_login = driver.find_element(By.NAME, "username")
    username_login_Display = username_login.is_displayed()
    try:
        assert username_login_Display == True
        username_login.send_keys("Admin")
    except AssertionError:
        print("User name is no Available")

    time.sleep(3)
    password_login = driver.find_element(By.NAME, "password")
    password_login_enable = password_login.is_enabled()
    try:
        assert password_login_enable == True
        password_login.send_keys("admin123")
    except AssertionError:
        print("Password is not enabled")
        time.sleep(3)
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
        try:
            assert login_button.is_enabled()
            login_button.click()
        except AssertionError:
            print("Login Button is enable")
        time.sleep(3)
        Expected_Result = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        Actual_Result = driver.current_url
        try:
            assert Expected_Result == Actual_Result
            print("Text Result : Passed")
        except AssertionError:
            print("Text Result : Failed")
        driver.close()
        print("Text will be completed")
Webelememt_State()










