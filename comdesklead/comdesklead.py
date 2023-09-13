import csv
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# chrome起動設定
chrome_options = webdriver.chrome.options.Options()

chrome_options.binary_location = r'C:\Program Files\chromebinary\chrome.exe'
driver_path = r'C:\Program Files\chromedriver\chromedriver.exe'

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 探索するURLを指定する
url = "https://usengroup.comdesk.com/auth"
driver.get(url)

# sleep5秒
sleep(5)

# IDとPASS
user_id = driver.find_element(by=By.NAME, value="user_id")
password = driver.find_element(by=By.NAME, value="password")

user_id.clear()
password.clear()

user_id.send_keys("")
password.send_keys("")

sleep(1)

# log in 処理
login_button = driver.find_element(by=By.ID, value="login_btn")
login_button.click()

sleep(10)

# モーダルをclose
modal_close = driver.find_element(by=By.CLASS_NAME, value="close")
modal_close.click()

sleep(10)

# driver quit
driver.quit()
