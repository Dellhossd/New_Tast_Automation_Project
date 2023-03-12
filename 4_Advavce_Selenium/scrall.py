import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Scralling():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.apple.com/')
    time.sleep(3)
    # Scrall to  the button
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    #scrall back to top
    driver.execute_script('window.scrollTo(0,0)')
    time.sleep(3)
    #scroll to specific element
    iPad = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[data-unit-id='ipad'] .unit-wrapper > [target]")))
    driver.execute_script("arguments[0].scrollIntoView(true)", iPad)
    time.sleep(3)






    driver.close()
Scralling()


