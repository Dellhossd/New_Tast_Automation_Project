from selenium import webdriver

import time
from  selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)
driver.get("https://www.walmart.com/account/login")
email_ID = driver.find_element(By.NAME,"Email Address")
if email_ID is None:
     print("Login ID")
else:
     print("Email add show incorrect")
driver.find_element(By.CSS_SELECTOR,"#sign-in-form > button")


time.sleep(3)
driver.close()

