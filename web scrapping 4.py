import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
str = soup.div.a.button.span
print(str.string)