from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def Web_Element_Statee():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    Username = driver.find_element(By.NAME,"username")
    Display_State = Username.is_displayed()
    try:
        assert Display_State == True
        Username.send_keys("Admin")
    except AssertionError:
        print("Username is not Available")
        time.sleep(3)




    Password = driver.find_element(By.NAME, "password")
    Enabled_State  = Password.is_enabled()
    try:
        assert Enabled_State == True
        Password.send_keys("admin123")
    except AssertionError:
        print("Password is not Enabled")
    time.sleep(3)

    Loging_Button = driver.find_element(By.CSS_SELECTOR,".orangehrm-login-button")
    try:
        assert Loging_Button.is_enabled()
        Loging_Button.click()
    except AssertionError:
        print("Login Button is not Enabled")
    time.sleep(3)






    Expected_Result = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    Actual_Result = driver.current_url
    try:
        assert Expected_Result == Actual_Result
        print("Text Result : Passed")
    except AssertionError:
        print("Text Result : Failed")

    driver.close()
    print("Text will be Complete")

Web_Element_Statee()
