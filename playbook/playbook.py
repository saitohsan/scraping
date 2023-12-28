import csv
import time
import os
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from google_chat import GoogleChat

# chat通知初期化
chat = GoogleChat("https://chat.googleapis.com/v1/spaces/AAAAhNlAZoc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=c_skCh03a3b_YAx9xdvwcm2nPbcEEaig1eU8BixfVds")

# 処理開始
chat.postText("playbook履歴取得処理開始")

try:

    # chrome起動設定
    chrome_options = webdriver.chrome.options.Options()

    chrome_options.binary_location = r'C:\Program Files\chromebinary\chrome.exe'
    driver_path = r'C:\Program Files\chromedriver\chromedriver.exe'

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 探索するURLを指定する
    url = "https://usen-next.magicmoment.co.jp/auth/"
    driver.get(url)

    # 最大化しないと要素が見つからない場合がある
    driver.maximize_window()

    # 描画待機5秒
    sleep(5)

    # IDとPASS
    user_id = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[2]/div[1]/div/input")
    password = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[2]/div[2]/div/div/input")

    # clear
    user_id.clear()
    password.clear()

    ### ### ###
    ### playbookのログインIDとパスワード
    ### ### ###
    # ID/PASS入力
    user_id.send_keys("")
    password.send_keys("")

    # 描画待機10秒
    sleep(10)

    # ログイン処理
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/form/div[4]/button/span[1]")
    login_button.click()

    # 画面描画待機
    sleep(5)
except:
    chat.postText("ログイン処理失敗")


try:
    # エンゲージメントに遷移
    engagement_url = "https://usen-next.magicmoment.co.jp/engagement"
    driver.get(engagement_url)

    # 画面描画待機
    sleep(5)

    # ダウンロード用に遷移
    #download_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[1]/div[1]/section[3]/div[1]")
    #download_element.click()
    download_url = "https://usen-next.magicmoment.co.jp/engagement?viewId=6efedb66-9fcb-11ee-af38-1aa6aa03d55f"
    driver.get(download_url)

    # 画面描画待機
    sleep(15)

    # 詳細検索を押下
    detail_search_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[4]/button/span[1]")
    detail_search_button.click()

    # 条件設定はシステムに記憶させたので省略

    # 画面描画待機
    #sleep(5)

    # 最終対応からの期間
    # カスタムを選択
    #custome_selecter = driver.find_element(By.ID, "react-select-8-input")
    #custome_selecter.click()
    #custome_selecter.send_keys('カスタム')
    # 選択肢の増減が怖いので
    #custome_selecter.send_keys(Keys.DOWN)
    # 5回押しはやめる
    #custome_selecter.send_keys(Keys.ENTER)

    # 画面描画待機（新要素出現）
    sleep(10)

    # 24時間以内
    #hour_setter = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[2]/div/div/div/div[7]/div[2]/div[2]/div[3]/input")
    #hour_setter.click()
    #hour_setter.send_keys(24)

    # 画面描画待機
    sleep(10)
except:
    chat.postText("画面条件設定失敗")

# 1店舗目受注商材入力

try:
    # 出力ボタンを押す
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[5]/div/div/button")
    output_button.click()

    sleep(10)

    # 出力選択肢を押す
    output_element = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div[3]/div/div[2]/div[2]/div/div[2]")
    output_element.click()

    sleep(10)

    # プレイブックプルダウン
    playbook_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/input")
    playbook_input.click()

    sleep(5)

    playbook_input.send_keys("1店舗")
    playbook_input.send_keys(Keys.ENTER)

    sleep(5)

    # 文字コードプルダウン
    character_code_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/div[2]/input")
    character_code_input.click()

    sleep(5)

    character_code_input.send_keys(Keys.DOWN)
    character_code_input.send_keys(Keys.ENTER)

    sleep(5)

    # 出力押下
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[3]/div/div[2]/div/button")
    output_button.click()

    sleep(10)
except:
    chat.postText("1店舗目受注商材入力の出力失敗")

# 2店舗目受注商材入力

try:
    # 出力ボタンを押す
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[5]/div/div/button")
    output_button.click()

    sleep(10)

    # 出力選択肢を押す
    output_element = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div[3]/div/div[2]/div[2]/div/div[2]")
    output_element.click()

    sleep(10)

    # プレイブックプルダウン
    playbook_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/input")
    playbook_input.click()

    sleep(5)

    playbook_input.send_keys("2店舗")
    playbook_input.send_keys(Keys.ENTER)

    sleep(5)

    # 文字コードプルダウン
    character_code_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/div[2]/input")
    character_code_input.click()

    sleep(5)

    character_code_input.send_keys(Keys.DOWN)
    character_code_input.send_keys(Keys.ENTER)

    sleep(5)

    # 出力押下
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[3]/div/div[2]/div/button")
    output_button.click()

    sleep(10)
except:
    chat.postText("2店舗目受注商材入力の出力失敗")


# 3店舗目受注商材入力

try:
    # 出力ボタンを押す
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[5]/div/div/button")
    output_button.click()

    sleep(10)

    # 出力選択肢を押す
    output_element = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div[3]/div/div[2]/div[2]/div/div[2]")
    output_element.click()

    sleep(10)

    # プレイブックプルダウン
    playbook_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/input")
    playbook_input.click()

    sleep(5)

    playbook_input.send_keys("3店舗")
    playbook_input.send_keys(Keys.ENTER)

    sleep(5)

    # 文字コードプルダウン
    character_code_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/div[2]/input")
    character_code_input.click()

    sleep(5)

    character_code_input.send_keys(Keys.DOWN)
    character_code_input.send_keys(Keys.ENTER)

    sleep(5)

    # 出力押下
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[3]/div/div[2]/div/button")
    output_button.click()

    sleep(10)
except:
    chat.postText("3店舗目受注商材入力の出力失敗")


# 4店舗目受注商材入力

try:
    # 出力ボタンを押す
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[5]/div/div/button")
    output_button.click()

    sleep(10)

    # 出力選択肢を押す
    output_element = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div[3]/div/div[2]/div[2]/div/div[2]")
    output_element.click()

    sleep(10)

    # プレイブックプルダウン
    playbook_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/input")
    playbook_input.click()

    sleep(5)

    playbook_input.send_keys("4店舗")
    playbook_input.send_keys(Keys.ENTER)

    sleep(5)

    # 文字コードプルダウン
    character_code_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/div[2]/input")
    character_code_input.click()

    sleep(5)

    character_code_input.send_keys(Keys.DOWN)
    character_code_input.send_keys(Keys.ENTER)

    sleep(5)

    # 出力押下
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[3]/div/div[2]/div/button")
    output_button.click()

    sleep(10)
except:
    chat.postText("4店舗目受注商材入力の出力失敗")


# 5店舗目受注商材入力

try:
    # 出力ボタンを押す
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[5]/div/div/button")
    output_button.click()

    sleep(10)

    # 出力選択肢を押す
    output_element = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div[3]/div/div[2]/div[2]/div/div[2]")
    output_element.click()

    sleep(10)

    # プレイブックプルダウン
    playbook_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/input")
    playbook_input.click()

    sleep(5)

    playbook_input.send_keys("5店舗")
    playbook_input.send_keys(Keys.ENTER)

    sleep(5)

    # 文字コードプルダウン
    character_code_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/div[2]/input")
    character_code_input.click()

    sleep(5)

    character_code_input.send_keys(Keys.DOWN)
    character_code_input.send_keys(Keys.ENTER)

    sleep(5)

    # 出力押下
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[3]/div/div[2]/div/button")
    output_button.click()

    sleep(10)
except:
    chat.postText("5店舗目受注商材入力の出力失敗")


# 6店舗目受注商材入力

try:
    # 出力ボタンを押す
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/article[2]/div[1]/div[5]/div/div/button")
    output_button.click()

    sleep(10)

    # 出力選択肢を押す
    output_element = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div[3]/div/div[2]/div[2]/div/div[2]")
    output_element.click()

    sleep(10)

    # プレイブックプルダウン
    playbook_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/input")
    playbook_input.click()

    sleep(5)

    playbook_input.send_keys("6店舗")
    playbook_input.send_keys(Keys.ENTER)

    sleep(5)

    # 文字コードプルダウン
    character_code_input = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/div[2]/input")
    character_code_input.click()

    sleep(5)

    character_code_input.send_keys(Keys.DOWN)
    character_code_input.send_keys(Keys.ENTER)

    sleep(5)

    # 出力押下
    output_button = driver.find_element(By.XPATH, "/html/body/div[1]/aside[2]/div/div/div[3]/div/div[2]/div/button")
    output_button.click()

    sleep(10)
except:
    chat.postText("6店舗目受注商材入力の出力失敗")



# 処理終了
driver.quit()
chat.postText("playbook履歴取得処理終了")
