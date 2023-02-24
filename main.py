# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from selenium import webdriver

import time

driver = webdriver.Firefox()
time.sleep(5)
driver.maximize_window()
driver.get("https://google.com")
# fetch webpage title from browser
google_title = driver.title
print(google_title)
# verify title is correct
try:
   assert "Google3" in driver.title
except AssertionError:
    print(str(AssertionError) + "title is in correct")
time.sleep(5)
driver.close()
print("Test is Complete")

