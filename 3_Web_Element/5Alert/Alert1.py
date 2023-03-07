
#Dropdown Testing Coad

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def New_Dropdon():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.salesforce.com/form/demo/salesforce-products/?gclid=EAIaIQobChMIwajHrL3I_QIVM8qUCR0J5wUnEAAYASAAEgJH7PD_BwE&d=7010M000001ynfX&nc=7010M000002QR17&DCMP=KNC-Google&ef_id=EAIaIQobChMIwajHrL3I_QIVM8qUCR0J5wUnEAAYASAAEgJH7PD_BwE:G:s&s_kwcid=AL!4604!3!605326008619!e!!g!!salesforce&gclsrc=aw.ds")
    Dropdow_first  = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[name='CompanyCountry']"))))
    #Dropdow_first.click()
    First_Select =Dropdow_first.first_selected_option
    try:
        assert First_Select.is_selected, "Country/Region"
        print("Test Case Passed : First Select Working")
    except AssertionError:
        print("Test Case Failed : First Select is not Working")
    time.sleep(3)


    Dropdow_first.select_by_index(2)
    Option_1 =Dropdow_first.first_selected_option

    try:
        assert Option_1.is_selected, "2"
        print("Passed")
    except AssertionError:
        print("Failed")





    Expect_List = ["United States", "Afghanistan","Albania"]
    Actual_List =[]
    for opt in Dropdow_first.options:
        options_text=opt.text
        Actual_List.append(options_text)
    try:
        assert Actual_List==Expect_List
        print("Final Passed")
    except AssertionError:
        print("Final Failed")
    driver.close()
New_Dropdon()

