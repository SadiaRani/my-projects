from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(5)
search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search.send_keys("House of Dragon")
search.send_keys(Keys.ENTER)
time.sleep(2)
driver.get("https://www.hbo.com/house-of-the-dragon")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/article/section[6]/div/div/div/div[2]/section/div[1]/ul/li[1]/div/div/a").screenshot("C:/Users/lenovo/OneDrive/Desktop/New folder/pic.png")
