from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common import NoAlertPresentException
import time
def Drag_and_Drop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://material.angular.io/cdk/drag-drop/examples")
    time.sleep(3)

    """
    source = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"example-viewer#cdk-drag-drop-axis-lock  .docs-example-viewer-body.ng-star-inserted")))
    target = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"cdk-drag-drop-axis-lock-example .example-box:nth-of-type(2)")))
    moving= ActionChains(driver)
    moving.drag_and_drop(source,target).perform()
    time.sleep(3)
    """



    Source_Element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"cdk-drag-drop-axis-lock-example .example-box:nth-of-type(2)")))
    Targrt_Element= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"cdk-drag-drop-axis-lock-example .example-box:nth-of-type(1)")))
    action = ActionChains(driver)
    action.drag_and_drop(Source_Element,Targrt_Element).perform()

    time.sleep(3)
    driver.close()
    print("Test Completed")
Drag_and_Drop()
