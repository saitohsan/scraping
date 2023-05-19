from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeのWebDriverのパスを指定してインスタンスを作成
driver = webdriver.Chrome('C:\Program Files\chromedriver')

# 石垣島のトリップアドバイザーページを開く
url = 'https://www.tripadvisor.com/Restaurants-g298223-Ishigaki_Okinawa_Prefecture.html'
driver.get(url)

# urlを格納する配列
url_list = []

# ページ遷移しながらレストラン情報をスクレイピング
page = 1
while True:
    print("----- ページ", page, "-----")
    
    # ページが完全に読み込まれるまで待機（最大30秒）
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.ID, 'EATERY_LIST_CONTENTS')))

    # レストランの情報を取得
    restaurant_elements = driver.find_elements(by=By.CLASS_NAME, value="RfBGI")

    # 各レストランの情報を表示
    for element in restaurant_elements:
        name = element.find_element(by=By.TAG_NAME, value="a").text
        url = element.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
        url_list.append(url)
        print(name,url)

    # 「次へ」ボタンがあればクリックして次のページへ遷移
    next_button = driver.find_elements(By.CSS_SELECTOR, "a.next")
    if next_button and next_button[0].is_displayed():
        driver.execute_script("arguments[0].click();", next_button[0])
        page += 1
    else:
        break


# WebDriverを終了
driver.quit()
