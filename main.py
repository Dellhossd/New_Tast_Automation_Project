from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def login_doordash_valid():
    driver =webdriver.Firefox()
    time.sleep(3)
    driver.get("https://identity.doordash.com/auth?client_id=1699031494479676248&redirect_uri=https%3A%2F%2Fmerchant-portal.doordash.com%2Fdasher_auth_callback&response_type=code&scope=*&prompt=none&login_user=&device_id=&layout=dasher_web&state=4477b6f9-14f8-453a-b31f-67bbef780002&allowRedirect=true&failureRedirect=%2Fdasher%2Flogin&successRedirect=https%3A%2F%2Fwww.doordash.com%2Fdasher%2Fapplication&passReqToCallback=true")
    time.sleep(5)
    usename= driver.find_element(By.CSS_SELECTOR,"#FieldWrapper-0")
    usename.send_keys("hossaindell3@gmail.com")
    time.sleep(5)
    password =driver.find_element(By.CSS_SELECTOR,".Input__InputContainer-sc-1ips7db-1.fqQysI  .Input__InputContent-sc-1ips7db-3.ccVVEo")
    password.send_keys("Sara$$8443")
    time.sleep(10)
    signin_browser =driver.find_element(By.CSS_SELECTOR,".iPRQcJ.styles__TextElement-sc-3qedjx-0")
    signin_browser.click()
    time.sleep(3)
    ExpectURL = "https://www.doordash.com/dasher/application/EZb0rW6RYQ31497idkvruVnCY2FY3gd40Fp8kJR3k5vtgxnrcS/startOnBoardingWorkflow?"
    ActualURL = driver.current_url

    try:
        assert ExpectURL == ActualURL
        print("Valid Text Case Result: Pass")
    except AssertionError:
        print("Valid Text Cash Result : Failed")
    time.sleep(15)
    driver.close()
    print("Text Complete")
login_doordash_valid()