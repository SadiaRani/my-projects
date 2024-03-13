from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s= Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?sca_esv=2e3cbffe5a601d85&rlz=1C1SQJL_enPK1089PK1089&sxsrf=ACQVn0_PkWxyM3V6b7VclQ6s0ahe4BRU0w:1709362295221&q=pandas&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjdoJjj_tSEAxUIgf0HHUaQAEcQ0pQJegQIGBAB&biw=1366&bih=633&dpr=1")
time.sleep(2)
height = driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(4)