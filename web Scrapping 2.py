import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
#print(r)
soup =BeautifulSoup(r.text,"html.parser")
print (soup.div)

