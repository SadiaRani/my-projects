import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"html.parser")
table = soup.find("table",class_="ih-td-tab auction-tbl")
#print(table)
header = table.find_all("th",class_="skip-filter")
#print(header)
table_heading =[]
for i in header:
    title = i.text
    table_heading.append(title)
#print(table_heading)
df = pd.DataFrame(columns=table_heading)
#print(df)
rows = table.find_all("tr")
#print(rows)
for i in rows[1:]:
    data =i.find_all("td")
    #print(data)
    row = [tr.text.strip().replace('\n','') for tr in data]
    #print(row)
    l = len(df)
    df.loc[l]=row
print(df)
df.to_csv("Tata ipl Auction 2022.csv")