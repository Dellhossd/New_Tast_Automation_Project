from selenium import webdriver

import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)
driver.get("https://goolel.com")
time.sleep(3)
driver.get("https://apple.com")
time.sleep(3)
driver.back()
print(driver.title)
time.sleep(3)
driver.forward()
print(driver.title)
time.sleep(3)
driver.refresh()
print(driver.title)
driver.close()
