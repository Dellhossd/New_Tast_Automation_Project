from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def Dropdown_Select():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/dropdown')
    dropdown = Select(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"dropdown"))))

    default_Selected= dropdown.first_selected_option
    try:
        assert default_Selected.is_selected, "Please select an option"
        print("Default Selected is Correct : Test Passed 1")
    except AssertionError:
        print("Default Selected is incorrect : Text Failed 1")
    time.sleep(3)

    dropdown.select_by_index("2")
    Sara_Selected = dropdown.first_selected_option

    try:
        assert Sara_Selected.is_selected, "2"
        print("Option 1 New is Selected : Test will be Passed")
    except AssertionError:
        print("Option 1 New is not Selected : Text will be Failed")
    time.sleep(3)

    dropdown.select_by_visible_text("Option 1")  # Accept String Values
    Dell_Selected = dropdown.first_selected_option
    try:
        assert Dell_Selected.is_selected, "Option 1"
        print("Option 2 is  Selected : Test Passed")
    except AssertionError:
        print("Option 2 is not Selected : Text Failed")
    time.sleep(3)




    Expected_Options_List = ["Please select an option", "Option 1", "Option 2"]
    Actual_Options_List = []
    for opttion in dropdown.options:

        Dell_hero = opttion.text
        Actual_Options_List.append(Dell_hero)
    try:
        assert Actual_Options_List == Expected_Options_List
        print("All Options List Test Passed")
    except AssertionError:
        print("All Options List Text Failed")
    time.sleep(3)
    driver.close()
    print("Finale Text Completed")
Dropdown_Select()











