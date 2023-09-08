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
url = "https://usengroup.comdesk.com/auth"
driver.get(url)

# sleep10秒
sleep(10)


# driver quit
driver.quit()
