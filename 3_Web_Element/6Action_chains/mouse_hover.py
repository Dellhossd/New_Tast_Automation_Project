from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains

import time

def Mouse_hoiver_Demo():
    driver =webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/")
    Meno_Desktops = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Desktops")))
    time.sleep(3)

    action = ActionChains(driver)
    action.move_to_element(Meno_Desktops).perform()

    submano_mac1 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Mac (1)")))
    submano_mac1.click()
    try:
        assert "Mac" in driver.title
        print("Mac Page Found")
    except AssertionError:
        print("Mac Page not Found")
        time.sleep(3)
    Desktop = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Desktops")))
    time.sleep(3)

    New_Action =ActionChains(driver)
    New_Action.move_to_element(Desktop).perform()
    Pc =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"PC (0)")))
    Pc.click()
    try:
        assert "PC" in driver.title
        print("Pc Page Open")
    except AssertionError:
        print("Pc Page not Open")




    time.sleep(3)
    driver.close()
    print("Test Case Completed")
Mouse_hoiver_Demo()

