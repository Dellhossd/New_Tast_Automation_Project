from selenium import webdriver

import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)

# Step 1. open Google Browser
driver.get("https://google.com")
time.sleep(3)
# Step 2. go to another browser Apple
driver.get("https://apple.com")
time.sleep(3)
# Step 3. back to Google
driver.back()
print(driver.title)#Google
time.sleep(3)
#  Step 4.forward to apple
driver.forward()
print(driver.title) #Apple
time.sleep(3)
# Step 5. Refresh apple
driver.refresh()
print(driver.title)
driver.close()