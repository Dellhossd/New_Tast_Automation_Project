import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Upload_File():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/upload")
    time.sleep(3)
    Choose_File_Button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"file-upload")))
    File_Path = "D:\\file\\Research Paper #3.docx"

    try:
        Choose_File_Button.send_keys(File_Path)
        print("File Available")
        upload_file = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"file-submit")))
        upload_file.click()
        success_message = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h3")))
        try:
            assert "File Uploaded!" in success_message.text
            print("Test Passed: File Uploaded!" )
        except AssertionError:
            print("Test Failed: File didn't  Uploaded!")
    except Exception:
        print("File Not Available.Exception:" +str(Exception))
    driver.close()
Upload_File()




