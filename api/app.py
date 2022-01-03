from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

Chrome =  webdriver.Chrome()
driver = Chrome

url = "https://kan.run/"
# url = input("URLを入力してください: ")

driver.get("https://web.archive.org/")
time.sleep(1)
print("1")
do_input = driver.find_element(by=By.NAME, value="url_preload")

do_input.send_keys(url)
do_input.send_keys(Keys.RETURN)
print("2")

time.sleep(2)

submit_button = driver.find_element(by=By.CLASS_NAME, value="web-save-button")
submit_button.send_keys(Keys.RETURN)
print("3")

time.sleep(5)