from selenium import webdriver

import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(10)
driver.get("https://google.com")
# fetch webpage title from browser
google_title = driver.title
print(google_title)
# verify title is correct

try:
     assert "Google2" in driver.title
except AssertionError:
    print(str(AssertionError) + "title is incorrect!!!")

time.sleep(10)
driver.close()
print("test is complete")