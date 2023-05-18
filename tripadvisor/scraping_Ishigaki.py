from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeのWebDriverのパスを指定してインスタンスを作成
driver = webdriver.Chrome('パス/to/chromedriver')

# 石垣島のトリップアドバイザーページを開く
driver.get('https://www.tripadvisor.com/Restaurants-g298223-Ishigaki_Okinawa_Prefecture.html')

# レストランの情報を取得する関数
def scrape_restaurant_info(element):
    name_element = element.find_element(By.CSS_SELECTOR, "a._15_ydu6b")
    name = name_element.text if name_element else ""
    rating = element.find_element(By.CSS_SELECTOR, "span.ui_bubble_rating").get_attribute('alt')
    reviews = element.find_element(By.CSS_SELECTOR, "span.reviewCount").text
    cuisine = element.find_element(By.CSS_SELECTOR, "div._1p0FLy4t").text

    print("レストラン名:", name)
    print("評価:", rating)
    print("口コミ数:", reviews)
    print("料理ジャンル:", cuisine)
    print("--------------------------------------")

# ページ遷移しながらレストラン情報をスクレイピング
page = 1
while True:
    print("----- ページ", page, "-----")
    
    # ページが完全に読み込まれるまで待機（最大30秒）
    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.ID, 'EATERY_LIST_CONTENTS')))

    # レストランの情報を取得
    restaurant_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-test-target='restaurants-list'] div._1llCuDZj")

    # 各レストランの情報を表示
    for element in restaurant_elements:
        scrape_restaurant_info(element)

    # 「次へ」ボタンがあればクリックして次のページへ遷移
    next_button = driver.find_elements(By.CSS_SELECTOR, "a.next")
    if next_button and next_button[0].is_displayed():
        driver.execute_script("arguments[0].click();", next_button[0])
        page += 1
    else:
        break


# WebDriverを終了
driver.quit()
