import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def headless():
    firexfox_options= Options()
    firexfox_options.add_argument ('--headless')
    driver = webdriver.Firefox(options=firexfox_options)





    driver.get("https://google.com")
    time.sleep(3)
    print(driver.title)
    driver.execute_script("window.open('https://apple.com')")
    time.sleep(3)
    driver.execute_script("window.open('https://www.walmart.com/')")
    time.sleep(3)
    total_window = driver.window_handles
    print(total_window)
    driver.switch_to.window(total_window[1])
    print("Switch to New Window:" + driver.title)
    time.sleep(3)
    driver.switch_to.window(total_window[2])
    time.sleep(3)
    print("Switch to another Window:" + driver.title)
    time.sleep(3)
    driver.switch_to.window(total_window[0])
    print("Switch to old Window:" + driver.title)
    time.sleep(3)
    print()
    driver.quit()
headless()