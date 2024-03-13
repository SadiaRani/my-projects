from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s = Service (chrome_driver_path)
driver =webdriver.Chrome(service=s)
driver.get("https://www.flipkart.com/")
time.sleep(4)
search =driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input")
search.send_keys("kids toys")
search.send_keys(Keys.ENTER)