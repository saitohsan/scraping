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
url = "https://www.tripadvisor.jp/Restaurants-g298223-Ishigaki_Okinawa_Prefecture.html"
driver.get(url)

# CSVに書き込む準備
# CSVヘッダ
csv_header = ['オーナー登録済フラグ','店名','住所','電話番号','ジャンル','評価＆口コミ点数','口コミ数','公式サイトURL','メニューURL','URL']

# 最終的に書き込むデータ2次元配列
restaurant_info_List = []
restaurant_info_List.append(csv_header)

# shopの個別URLだけを格納しておく配列
restaurant_url_List = []

# restaurant一覧、URLを取得（1ページ目）
class_group = driver.find_elements(by=By.CLASS_NAME, value="RfBGI")
for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="a").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    restaurant_url_List.append(url_link)

# 次へをクリック
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# restaurant一覧、URLを取得（2ページ目）
class_group = driver.find_elements(by=By.CLASS_NAME, value="RfBGI")
for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="a").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    restaurant_url_List.append(url_link)

# 次へをクリック
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# restaurant一覧、URLを取得（3ページ目）
class_group = driver.find_elements(by=By.CLASS_NAME, value="RfBGI")
for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="a").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    restaurant_url_List.append(url_link)

    
# driverを終了する
driver.quit()

# URLを順番にあけて、必要な情報をあつめる
for target_url in restaurant_url_List:
    # URLを開く
    driver.get(target_url)

    # 10秒待機
    sleep(10)

    # 要素取得
    # csv_header = ['オーナー登録済フラグ','店名','住所','電話番号','ジャンル','評価＆口コミ点数','口コミ数','公式サイトURL','メニューURL','URL']
    owner_flg = driver.find_element(by=By.CLASS_NAME, value="XAnbq _S ZUJme").text
    restaurant_name = driver.find_element(by=By.CLASS_NAME, value="HjBfq").text

    print(owner_flg,restaurant_name)

    driver.quit()

