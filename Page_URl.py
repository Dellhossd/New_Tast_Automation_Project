from selenium import webdriver

import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)

driver.get("https://google.com")
google_title = driver.title
print(google_title)
# verify title tast
try:
    assert "Google2" in driver.title
except AssertionError:
    print(str(AssertionError)  + "If title is incorrect")
time.sleep(3)
print("Tast will complete show ")
time.sleep(3)
driver.close()