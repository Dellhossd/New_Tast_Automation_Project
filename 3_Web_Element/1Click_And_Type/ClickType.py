from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Begaining of the test Everyone has to floew the all Step or Test case:-
      #Step1 :- Launch the Browser
      #Step2 :- Go to the Login Page
      #Step3 :- Enter Username
      #Step4 :- Enter Password
      #Step5 :- Click Login Button
      #Step6 :- Clos the Button
      #Step7 :- Expect Result : Verify by URL
      #Step 8:- Actual Result : Verify by URL
      #Step9 :- Text Result
      #Step10:- Close the Browser
def Open_New_Browser_Texting_Valid():

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    username_login =driver.find_element(By.NAME,"username")
    username_login.send_keys("Admin")
    time.sleep(3)
    password_login = driver.find_element(By.NAME,"password")
    password_login.send_keys("admin123")
    time.sleep(3)
    login_button =driver.find_element(By.CSS_SELECTOR,".orangehrm-login-button")
    login_button.click()
    Expected_Result = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    Actual_Result = driver.current_url
    try:
        assert Expected_Result == Actual_Result
        print("Text Result : Passed")
    except AssertionError:
        print("Text Result : Failed")
    time.sleep(3)
    driver.close()
    print("Text will be completed")











def Open_New_Browser_Texting_Invalid():

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    username_login =driver.find_element(By.NAME,"username")
    username_login.send_keys("Admin12")
    time.sleep(3)
    password_login = driver.find_element(By.NAME,"password")
    password_login.send_keys("admin321")
    time.sleep(3)
    login_button =driver.find_element(By.CSS_SELECTOR,".orangehrm-login-button")
    login_button.click()
    time.sleep(3)
    Exp_Result = "Invalid credentials"
    Act_Result = driver.find_element(By.CSS_SELECTOR,".oxd-alert-content-text.oxd-text.oxd-text--p").text
    try:
        assert Exp_Result == Act_Result
        print("Test Passed")
    except AssertionError:
        print("Text Failed")


    time.sleep(3)
    driver.close()
    print("Text will be completed")
Open_New_Browser_Texting_Valid()
Open_New_Browser_Texting_Invalid()




