
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import Actionchain
import time

chrome_driver_path = "C:/Users/lenovo/OneDrive/Desktop/New folder/chromedriver-win32/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/")


# Corrected: Use find_element_by_xpath on the driver instance, not the service
phon_no =driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
phon_no.click()
# noinspection PyUnresolvedReferences
phon_no.send_keys("12345678910")
time.sleep(2)
login= driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
login.click()
time.sleep(10)

