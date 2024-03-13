import pandas as pd
import requests
from bs4 import BeautifulSoup
#url="https://www.oneindia.com/coronavirus-affected-cities-districts-in-india.html"
url = "https://ticker.finology.in/"
r= requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"html.parser")
table = soup.find("table",class_="table table-sm table-hover screenertable")
#print(table.text)
header = table.find_all("th")
#print(header)
#df.to_csv("product_market_data.csv ")
heading = []
for i in header:
    title = i.text
    heading.append(title)
#print(heading)

df = pd.DataFrame(columns = heading)
#print(df)
rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    #print(data)
    row =[tr.text.strip().replace('\n', '') for tr in data]
    #print(row)
    l = len(df)
    df.loc[l] = row
#print(df)
df.to_csv("Product_market_data.csv")

