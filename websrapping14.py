from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import Actionchain
import time
chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s=Service(chrome_driver_path)
driver= webdriver.Chrome(service = s)
driver.get("https://twitter.com/?lang=en")
time.sleep(4)
driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a").click()
time.sleep(4)

