from selenium import webdriver

import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(10)
driver.get("https://google.com")
time.sleep(10)
driver.close()