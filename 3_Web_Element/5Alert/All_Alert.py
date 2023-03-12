from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common import NoAlertPresentException

def Handel_Alert():
    driver =webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/javascript_alerts")

    Normal_Alert_Button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li:nth-of-type(1) > button")))
    Normal_Alert_Button.click()
    time.sleep(3)
    
    Normal_Alert= WebDriverWait(driver,10).until(EC.alert_is_present())


    try:
        assert Normal_Alert.text == "I am a JS Alert"
        print("Test 1) Passed : Normal Alert Button Open")
    except AssertionError:
        print("Test Failed : Normal Alert Button is not  Open")
    Normal_Alert.accept()


    Confirm_Alert_Button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li:nth-of-type(2) > button")))
    Confirm_Alert_Button.click()
    time.sleep(3)




    Confirm_Alert= WebDriverWait(driver,10).until(EC.alert_is_present())
    try:
        assert Confirm_Alert.text == "I am a JS Confirm"
        print("Test 2) Passed :Confirm Alert is Open")
    except AssertionError:
        print("Test 2) Failed :Confirm Alert is not Open")
    #Confirm_Alert.accept()
    Confirm_Alert.dismiss()



    Prompt_Alert_Button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > button")))
    Prompt_Alert_Button.click()
    time.sleep(5)
    Prompt_Alert =WebDriverWait(driver,10).until(EC.alert_is_present())
    try:
        assert Prompt_Alert.text == "I am a JS prompt"

        print("Test 3) Passed:Prompt Alert is Open")
        Prompt_Alert.send_keys('dddd')
    except AssertionError:
        print("Test 3) Failed :Prompt Alert is not Open")
    Prompt_Alert.accept()

    try:
        Alert_text = Normal_Alert.text=Confirm_Alert.text
        assert False, "Test Failed.Alert still open"
    except NoAlertPresentException:
        print("Test Passed.Normal Alert closed.")

        pass
    time.sleep(5)



    driver.close()


    print("Test Case could be Passed")
Handel_Alert()


