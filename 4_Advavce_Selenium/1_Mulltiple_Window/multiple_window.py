import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoAlertPresentException

def Switch_Multiple_Windows():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    time.sleep(3)
    #assert "Google" in driver.title
    print(driver.title)
    driver.execute_script("window.open('https://www.walmart.com/')")
    time.sleep(3)
    print(driver.title)
    driver.execute_script("window.open('https://apple.com')")
    print(driver.title)
    time.sleep(3)
    total_window =driver.window_handles
    print(total_window)
    time.sleep(3)

    driver.switch_to.window(total_window[1])
    time.sleep(3)
    #assert "Apple" in driver.title
    print(" Switch to new window:" + driver.title)
    time.sleep(3)
    #driver.switch_to.window([1])
    #print("Switch to middal window" + driver.title)
    #time.sleep(3)

    driver.switch_to.window(total_window[0])
    #assert "Googl" in driver.title
    print("Switch to old window:"    + driver.title)
    time.sleep(3)
    driver.quit()







Switch_Multiple_Windows()


