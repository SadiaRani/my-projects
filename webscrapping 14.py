from  selenium import webdriver
from selenium .webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s=Service(chrome_driver_path)
driver = webdriver.Chrome(service = s)
driver.get("https://www.wscubetech.com/")
time.sleep(2)
#driver.save_screenshot("C://Users//lenovo//OneDrive//Desktop//New folder//full-page.png")
driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div[2]/img").screenshot("C://Users//lenovo//OneDrive//Desktop//New folder//logo.png")