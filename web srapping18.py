from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s= Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.ajio.com/s/footwear-4792-56592?query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Flip%20Flop%20%26%20Slippers%3Al1l3nestedcategory%3AWomen%20-%20Flip%20Flop%20%26%20Slippers&curated=true&curatedid=footwear-4792-56592&gridColumns=3")
time.sleep(4)
while True:
    Height = driver.execute_script("return document.body.scrollHeight")
    print(Height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")       
    new_height = driver.execute_script("return document.body.scrollHeight")
    if Height==new_height:
        break
