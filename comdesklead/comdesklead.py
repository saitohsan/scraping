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
user_id = driver.find_elements(by=By.NAME, value="user_id")
password = driver.find_elements(by=By.NAME, value="password")

user_id.clear()
password.clear()

sleep(5)

# driver quit
driver.quit()
