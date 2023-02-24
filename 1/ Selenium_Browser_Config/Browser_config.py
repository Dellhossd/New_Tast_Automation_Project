from selenium import webdriver

import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(5)
driver.get("https://google.com")
driver.set_window_size(300,800)
time.sleep(5)
x = driver.get_window_size()
print(x)
driver.close()