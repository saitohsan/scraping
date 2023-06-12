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
url = "https://www.tripadvisor.jp/Restaurants-g298207-zft21269-Fukuoka_Fukuoka_Prefecture_Kyushu.html"
driver.get(url)

# CSVに書き込む準備
# CSVヘッダ
csv_header = ['オーナー登録済フラグ','店名','住所','電話番号','ジャンル','評価＆口コミ点数','口コミ数','公式サイトURL','メニューURL','URL']

# 最終的に書き込むデータ2次元配列
restaurant_info_List = []
restaurant_info_List.append(csv_header)

# shopの個別URLだけを格納しておく配列
restaurant_url_List = []

# sleep
sleep(10)

# 次へをクリック（1から2）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（2から3）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（3から4）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（4から5）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（5から6）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（6から7）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（7から8）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（8から9）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（9から10）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（10から11）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（11から12）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（12から13）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（13から14）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（14から15）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（15から16）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（16から17）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（17から18）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（18から19）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（19から20）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（20から21）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（21から22）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（22から23）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（23から24）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（24から25）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（25から26）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（26から27）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（27から28）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（28から29）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（29から30）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（30から31）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（31から32）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（32から33）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（33から34）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（34から35）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（35から36）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（36から37）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（37から38）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（38から39）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（39から40）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)

# 次へをクリック（40から41）
next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

# 10秒待機
sleep(10)




# restaurant一覧、URLを取得（41ページ目）
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

# restaurant一覧、URLを取得（42ページ目）
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

# restaurant一覧、URLを取得（43ページ目）
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

# restaurant一覧、URLを取得（44ページ目）
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

# restaurant一覧、URLを取得（45ページ目）
class_group = driver.find_elements(by=By.CLASS_NAME, value="RfBGI")
for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="a").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    restaurant_url_List.append(url_link)



# URL格納チェック
for a in restaurant_url_List:
    print(a)

sleep(10)

# URLを順番にあけて、必要な情報をあつめる
for target_url in restaurant_url_List:
    # URLを開く
    driver.get(target_url)

    # 10秒待機
    sleep(10)

    # 個別レストラン情報を格納する配列
    restaurant_info = []

    # 要素取得
    # csv_header = ['オーナー登録済フラグ','店名','住所','電話番号','ジャンル','評価＆口コミ点数','口コミ数','公式サイトURL','メニューURL','URL']
    try:
        owner_flg = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div').text
    except:
        owner_flg = ''
    try:
        restaurant_name = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[1]/h1').text
    except:
        restaurant_name = ''
    try:
        address = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[1]/span/a').text
    except:
        address = ''
    try:
        tel = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[2]/span/span[2]/a').text
    except:
        tel = ''
    try:
        genre = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[2]/span[3]/a[2]').text
    except:
        genre = ''
    try:
        score = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span[1]').text
    except:
        score = ''
    try:
        kuchikomi = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/a').text
    except:
        kuchikomi = ''
    try:
        weburl = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[3]/span/a').get_attribute('href')
    except:
        weburl = ''
    try:
        menuurl = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[4]/a').get_attribute('href')
    except:
        menuurl=''

    
    
    # 配列に格納
    restaurant_info.append(owner_flg)
    restaurant_info.append(restaurant_name)
    restaurant_info.append(address)
    restaurant_info.append(tel)
    restaurant_info.append(genre)
    restaurant_info.append(score)
    restaurant_info.append(kuchikomi)
    restaurant_info.append(weburl)
    restaurant_info.append(menuurl)
    restaurant_info.append(target_url)
    
    # 出力用配列に格納
    restaurant_info_List.append(restaurant_info)
    print(restaurant_info)
    sleep(10)

driver.quit()

# csv出力
csv_path = r"fukuoka_izakaya5.csv"
with open(csv_path, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(restaurant_info_List)
