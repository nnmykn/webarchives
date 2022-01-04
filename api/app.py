from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fastapi import FastAPI
import time
import datetime


# Setup
options = webdriver.ChromeOptions()
options.add_argument('--headless')
Chrome =  webdriver.Chrome(chrome_options=options)
driver = Chrome

app = FastAPI()
# Setup end

# api system
@app.get("/save")
def do_save(p: str):
    url = p
    try:
        driver.get("https://web.archive.org/")
        time.sleep(1)
        print("1")
        do_input = driver.find_element(by=By.NAME, value="url_preload")

        do_input.send_keys(url)
        do_input.send_keys(Keys.RETURN)
        print("2")

        time.sleep(0.5)

        submit_button = driver.find_element(by=By.CLASS_NAME, value="web-save-button")
        submit_button.send_keys(Keys.RETURN)
        print("3")
        print("取得したサイトのURL:" + url)
        print("success!")
        return({"status": "success", "url": url})
    except:
        return({"status": "error"})

# api system end