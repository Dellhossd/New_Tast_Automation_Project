from selenium import webdriver

import time

browser = webdriver.Firefox()
browser.maximize_window()
time.sleep(10)
browser.get("https://google.com")
time.sleep(10)
browser.close()