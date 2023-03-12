import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def browser_customize_arguments():   # I had Problem wit Chrome
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--window-size=400,300')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=chrome_options)

    time.sleep(10)

    """chromeOptions.addArguments("--headless");
    chromeOptions.addArguments("start-maximized");
    chromeOptions.addArguments("--disable-gpu");
    chromeOptions.addArguments("--start-fullscreen");
    chromeOptions.addArguments("--disable-extensions");
    chromeOptions.addArguments("--disable-popup-blocking");
    chromeOptions.addArguments("--disable-notifications");
    chromeOptions.addArguments("--window-size=1920,1080");
    chromeOptions.addArguments("--no-sandbox");
    chromeOptions.addArguments("--dns-prefetch-disable");
    chromeOptions.addArguments("enable-automation");
    chromeOptions.addArguments("disable-features=NetworkService");"""


browser_customize_arguments()
