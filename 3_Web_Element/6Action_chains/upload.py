from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoAlertPresentException
import time


def Upload_File():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/upload")
    time.sleep(3)

    Choose_File_Button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"file-upload")))
    File_Path  = ("C:\\file\\New Downlodad.jpg")
    try:
        Choose_File_Button.send_keys(File_Path)
        print("Pass")
        Upload_Button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'file-submit')))
        Upload_Button.click()

        Success_Message = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h3")))
        try:
           assert "File Uploaded!" in Success_Message.text
           print("Test Case Passed : File Successfully Upload")
        except AssertionError:
            print("Test Case Failed : File not Upload")

    except Exception:
        print("Faill" + str(Exception))
    driver.close()
    print("Test Completed")
Upload_File()




