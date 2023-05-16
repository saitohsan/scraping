from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

#chromeドライバのパス指定
driver_path = "C:\Program Files\chromedriver"
chrome_service = fs.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)

url = "https://www.tripadvisor.jp/Restaurants-g298223-Ishigaki_Okinawa_Prefecture.html"
driver.get(url)

# restaurant一覧、URLを取得
class_group = driver.find_elements(by=By.CLASS_NAME, value="RfBGI")
for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="a").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    print(title, url_link)

next_button = driver.find_element(by=By.LINK_TEXT, value="次へ")
next_button.click()

for elem in class_group:
    title = elem.find_element(by=By.TAG_NAME, value="a").text
    url_link = elem.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    print(title, url_link)

    
# driverを終了する
driver.quit()