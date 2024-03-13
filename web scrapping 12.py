import pandas as pd
import requests
from  bs4 import BeautifulSoup
Names = []
Prices = []
Description = []
Reviews = []
url ="https://www.airbnb.co.in/new-delhi-india/stays"
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text,"html.parser")
#print(soup)
np = soup.find("a",class_="l1ovpqvx").get("href")
print(np)

name = soup.find_all("div",class_="t1jojoys" )
#print(name)
for i in name:
    nam = i.text
    Names.append(nam)
print(len(Names))
pric = soup.find_all("span",class_="_tyxjp1")
for i in pric:
    housp = i.text
    Prices.append(housp)
print(len(Prices))
desc = soup.find_all("div",class_="fb4nyux")
#for i in desc:
    #hdesc= i.text
    #Description.append(hdesc)
#print(len(Description))
reviw = soup.find_all("span", class_="r1dxllyb")
for i in reviw:
    Hosereview = i.text
    Reviews.append(Hosereview)
print(len(Reviews))

df = pd.DataFrame({"Name":Names,"Price":Prices,"Reviews":Reviews})
#print(df)
df.to_csv("Airbnd.csv")
#Nextpage = soup.find("a",class_="l1ovpqvx").get("href")
#print(Nextpage)
#cp = "https://www.airbnb.co.in/"+Nextpage
#print(cp)



