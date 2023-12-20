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

# 各ページを回ってURLだけ取得する
# 回遊設定 pageCounterは実際より＋１すること
pageCounter = 2

# 最後に探索しにいくURLリスト作成定義
urlList = []

# 出力するcsvファイル用配列
outputData = []

# URLだけとってくる
for num in range(1,pageCounter):
    url = "https://baseconnect.in/companies/category/56705ce0-0fe4-40cb-9659-68f5eaa45d27?page="+str(num)
    driver.get(url)

    # 最大化しないと要素が見つからない場合がある
    driver.maximize_window()

    # 描画待機3秒
    sleep(3)

    # リンク取得
    urlElements = driver.find_elements(By.CLASS_NAME, "searches__result__list__header__title")

    for element in urlElements:
        urlLink = element.find_element(By.TAG_NAME, value="a")
        url = urlLink.get_attribute("href");
        urlList.append(url)

# 取ってきたURLを探索して情報を取得する
for url in urlList:
    driver.get(url)

    # 最大化
    driver.maximize_window()

    # 描画待機3秒
    sleep(5)

    # 一時配列
    companyInfo = []

    # 会社名
    tempCompanyName = driver.title.split('｜')
    companyName = tempCompanyName[0]

    # 本社住所

    # 従業員数

    # 詰め込み
    companyInfo.append(companyName)

    print(companyInfo)

    sleep(5)

