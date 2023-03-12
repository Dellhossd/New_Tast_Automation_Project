import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
def final():
    driver=webdriver.Chrome()
    driver.get("https://www.samsung.com/us/")
    driver.maximize_window()
    time.sleep(1)
    parent_handle=driver.current_window_handle
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.apple.com/")
    driver.set_window_size(700,500)
    driver.maximize_window()
    print(driver.title)
    time.sleep(1)
    driver.back()
    expected_url="https://www.samsung.com/us/"
    actual_url=driver.current_url
    try:
        assert expected_url==actual_url
        print("Match")
    except:
        print("NOPE")


    search=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".gnb__search-btn-js.nv00-gnb__utility-btn > svg[role='presentation']")))
    search.click()
    inpuut=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#gnb-search-keyword"))).send_keys("S3")
    time.sleep(10)
    hit=driver.find_element(By.CSS_SELECTOR,"[an-tr='search layer--Image-submit'] [focusable]")
    hit.click()
    time.sleep(10)


    driver.forward()#does not forward to the apple page
    print(driver.title)
    time.sleep(2)
    print(driver.current_url)#why i have wrong url



    driver.execute_script("window.open('https://www.apple.com/')")
    child = driver.window_handles
    for handle in child:
        if handle != parent_handle:
            driver.switch_to.window(handle)

            applesearch=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".globalnav-link.globalnav-link-entertainment.globalnav-submenu-trigger-link > .globalnav-link-text-container")))
            action=ActionChains(driver)
            action.move_to_element(applesearch).perform()
            time.sleep(10)
            appleinput=driver.find_element(By.CSS_SELECTOR,"div#globalnav-submenu-link-entertainment .globalnav-submenu-group.globalnav-submenu-group-elevated > .globalnav-submenu-list > li:nth-of-type(1) > .globalnav-submenu-link")
            time.sleep(5)
            appleinput.click()

    driver.execute_script("window.open('https://us.trip.com/?locale=en_us')")
    newtab=driver.switch_to.window(driver.window_handles[2])
    print((newtab))
    small_business=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Attractions & Tickets")))
    small_business.click()
    time.sleep(2)





final()
