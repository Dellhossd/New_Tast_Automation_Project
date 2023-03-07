
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Wait_Dynamic():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    Usearname = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))
    try:
        assert Usearname.is_displayed()
        Usearname.send_keys("Admin")
    except AssertionError:
        print("Username is not Available")



    Password= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"password")))
    try:
        assert Password.is_enabled()
        Password.send_keys("admin123")
    except AssertionError:
        print("Password is not Enabled")




    Login_Button =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".orangehrm-login-button")))
    try:
        assert Login_Button.is_enabled()
        Login_Button.click()
    except AssertionError:
        print("Login Button is not Enabled")




    Expect_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    Actual_URL = driver.current_url
    try:
        assert Expect_URL== Actual_URL
        print("Valid Text Case Passed ")
    except AssertionError:
        print('Valid Text Case Failed')








    driver.close()
    print("Text will be completed")
Wait_Dynamic()




