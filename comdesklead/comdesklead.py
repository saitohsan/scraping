import csv
import time
import os
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# 最大化しないと要素が見つからない場合がある
driver.maximize_window()

# 描画待機5秒
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

# 画面描画待機
sleep(10)

# 今日の日付を入力
# 入力欄に直突っ込みすると、書式が崩れる。年月日で分けて入力
#input_date = datetime.datetime.now().strftime('%Y/%m/%d')

date_from = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[4]/div[1]/div/div[1]/div[4]/label/div/div/div/input")
date_from.send_keys(datetime.datetime.now().strftime('%Y'))
date_from.send_keys(Keys.TAB)
date_from.send_keys(datetime.datetime.now().strftime('%m'))
#date_from.send_keys(Keys.TAB) - 月を入れると自動でTAB移動するので省略
date_from.send_keys(datetime.datetime.now().strftime('%d'))

sleep(3)

date_to = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/div[1]/div/div[1]/div[5]/label/div/div/div/input')
date_to.send_keys(datetime.datetime.now().strftime('%Y'))
date_to.send_keys(Keys.TAB)
date_to.send_keys(datetime.datetime.now().strftime('%m'))
#date_to.send_keys(Keys.TAB) - 月を入れると自動でTAB移動するので省略
date_to.send_keys(datetime.datetime.now().strftime('%d'))

sleep(10)

# 指定ワークグループと、DL、ローカルファイルリネームの繰り返し処理
# Indeed

# ワークグループを1回クリック
workgrp_btn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/div[1]/div/div[1]/div[3]/button[1]/span[2]/p')
workgrp_btn.click()

# Indeedをクリック
indeed_box = driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/div[1]/div/div/div[3]/div[2]')
indeed_box.click()

# 適用押下
apply_btn = driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/div[2]/button[2]/span[2]/span')
apply_btn.click()

# 描画待機
sleep(5)

# ワークグループを1回クリック（戻す）
workgrp_btn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/div[1]/div/div[1]/div[3]/button[1]/span[2]/p')

# 待機
sleep(3)

# CSV DLボタンを押下

csv_dl_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/button/span[2]')
csv_dl_button.click()

# DL待機は10秒では不足
sleep(20)

# ローカルリネーム indeed
# 変更前ファイル
path1 = 'C:/Users/tak-saito/Downloads/calllog.csv'
path2 = 'C:/Users/tak-saito/Downloads/indeed_calllog.csv'
os.rename(path1,path2)

# driver quit
driver.quit()
