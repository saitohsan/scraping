import csv
import time
import datetime
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

# ログイン処理
login_button = driver.find_element(by=By.ID, value="login_btn")
login_button.click()

# 画面描画待機
sleep(10)

# 活動履歴へ遷移
history_url = "https://usengroup.comdesk.com/call_log"
driver.get(history_url)

sleep(10)

# 今日の日付を入力
today = datetime.date.today()
input_date = today.strftime('%Y/%m/%d')
date_from = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[4]/div[1]/div/div[1]/div[4]/label/div/div/div/input")
date_from.send_keys(input_date)

sleep(10)

# CSV DLボタンを押下


sleep(10)

# driver quit
driver.quit()
