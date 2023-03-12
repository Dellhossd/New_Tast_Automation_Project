import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
def New_Project():
    driver = webdriver.Firefox()
    driver.get("https://www.samsung.com/us/")
    driver.set_window_size(800,500)
    time.sleep(3)
    driver.maximize_window()
    time.sleep(5)
    Main_Url = driver.current_window_handle
    driver.get("https://www.apple.com")
    driver.maximize_window()
    print(driver.title)
    time.sleep(3)
    driver.back()
    print(driver.title)
    time.sleep(3)

    """driver.forward() # This forward link should be use After (Current_Url and Actual_url) 
    print(driver.title)
    time.sleep(3)"""
    current_url = "https://www.samsung.com/us/"
    actual_url= driver.current_url
    try:
        assert current_url == actual_url
        print("Pass")
    except AssertionError:
        print("Faild")
    time.sleep(3)
    """driver.forward()
    print(driver.title)
    print(driver.current_url)
    time.sleep(3)"""
    New_search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".search [focusable]"))).click()
    N_input =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gnb-search-keyword"))).send_keys("Galaxy Tab S8")
    time.sleep(3)
    driver.execute_script("window.open('https://www.walmart.com/')")
    Me = driver.window_handles
    for handal in Me:
        if handal !=Main_Url:
            driver.switch_to.window(handal)

    time.sleep(3)



    driver.quit()
    print("Test Completed")
New_Project()



