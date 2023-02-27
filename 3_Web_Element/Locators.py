from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)

# Step 1: Open Google link
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)


# Step 2. Find user input Field
username_field=driver.find_element(By.NAME,"username")
if username_field is not None:
    print("Dell")



# Step 3. Find password input Field
password_filed=driver.find_element(By.NAME,"password")
if password_filed is not None:
  print("Hossain")
else:
    print("this password should be incorrect")


# Step 3. Find Login button


Id_filed=driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button ")
if Id_filed is not None:
  print("yes")
  print("Finally Test will be completed")

driver.close()

