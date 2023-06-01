import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service as fs

# chromeドライバのパス指定
driver_path = "C:\Program Files\chromedriver"
chrome_service = fs.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)

# 探索するURLを指定する
url = "https://www.tripadvisor.jp/Restaurants-g298207-Fukuoka_Fukuoka_Prefecture_Kyushu.html"
driver.get(url)

# CSVに書き込む準備
# CSVヘッダ
csv_header = ['オーナー登録済フラグ','店名','住所','電話番号','ジャンル','評価＆口コミ点数','口コミ数','公式サイトURL','メニューURL','URL']

# 最終的に書き込むデータ2次元配列
restaurant_info_List = []
restaurant_info_List.append(csv_header)

# shopの個別URLだけを格納しておく配列
restaurant_url_List = []

# 居酒屋をクリック
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()


sleep(10)
driver.quit()
