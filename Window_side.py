from selenium import webdriver

import time
driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(3)
driver.get("https://google.com")



# step 1:get current window size
maximize_window_size = driver.get_window_size()
print("maximize_window_size: width ={}px, height ={}px".format(maximize_window_size['width'], maximize_window_size['height']))

#  step 2: set window
driver.set_window_size(485,800)
time.sleep(3)
set_window_size = driver.get_window_size()
print("set_window_size: width ={}px, height ={}px".format(set_window_size['width'], set_window_size['height']))

# step 3: verify window size

try:
    assert set_window_size['width'] == 1600 and set_window_size['height'] == 900, "window size is not 800*465"
    print("set window size correct")
except AssertionError:
   print(str(AssertionError) + 'If the window size is in correct then it  is incorrect')


time.sleep(3)
driver.close()
print('Test will be complete')