from selenium import webdriver
from selenium.webdriver.common.ny import By
from selenium.webdriver.chrome import service as fs

#chromeドライバのパス指定
driver_path = "C:\Users\tak-saito\Documents\chromedriver"
chrome_service = fs.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)

url = "https://www.google.com/?hl=ja"
driver.get(url)

# Google検索入力フォームに入力して送信
input_selector = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"    
input_element = driver.find_element(by=By.CSS_SELECTOR, value=input_selector)
input_element.send_keys("プログラミング pythonのお部屋")
input_element.submit()

# 検索結果の記事情報はclass="yuRUbf"に入っている
class_group = driver.find_elements(by=By.CLASS_NAME, value="yuRUbf")
for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="h3").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    print(title, url_link)
    
# driverを終了する
driver.quit()