from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def oringe_hrm_login_Valid():
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    username = driver.find_element(By.NAME,"username")
    username.send_keys("Admin")
    time.sleep(3)
    password_id = driver.find_element(By.NAME,"password")
    password_id.send_keys("admin123")
    time.sleep(3)
    loging_id =driver.find_element(By.CSS_SELECTOR,".orangehrm-login-action.oxd-form-actions > .orangehrm-login-button.oxd-button.oxd-button--main.oxd-button--medium")
    loging_id.click()
    Expected_Result = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    Actual_Result = driver.current_url
    try:
        assert Expected_Result == Actual_Result
        print("Valid Text Case Result :Passed")
    except AssertionError:
        print("Valid Text Case Result :Failed")

    time.sleep(3)
    driver.close()
    print("Text will be complete")






def oringe_hrm_login_Invalid():
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    username = driver.find_element(By.NAME, "username")
    username.send_keys("Admin12")

    time.sleep(3)
    password_id = driver.find_element(By.NAME, "password")
    password_id.send_keys("admin321")
    time.sleep(3)
    loging_id = driver.find_element(By.CSS_SELECTOR,
                                    ".orangehrm-login-action.oxd-form-actions > .orangehrm-login-button.oxd-button.oxd-button--main.oxd-button--medium")
    loging_id.click()
    Expected_URL = "Invalid credentials"
    Actual_URL = driver.current_url
    try:
        assert Expected_URL == Actual_URL
        print("Invalid Text Case Result :Passed")
    except AssertionError:
        print("Invalid Text Case Result :Failed")

    time.sleep(3)
    driver.close()
    print("Text will be complete")
oringe_hrm_login_Valid()
oringe_hrm_login_Invalid()

