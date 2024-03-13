import pandas as pd
import requests
from bs4 import BeautifulSoup

Name = []
Prices = []
description = []
review = []

for i in range(1, 11):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_3_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+under+50000&requestId=6a1dbc83-06db-4cf5-9da7-4c5f8f230993&page=" + str(i)
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    if box is None:
        # Skip processing for this page
        continue


    name = box.find_all("div", class_="_4rR01T")
    for i in name:
        mobiname = i.text
        Name.append(mobiname)
    print(len(Name))

    price = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in price:
        mobipric = i.text
        Prices.append(mobipric)
    print(len(Prices))

    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        mobidesc = i.text
        description.append(mobidesc)
    print(len(description))

    Review = box.find_all("div", class_="_3LWZlK")
    for i in Review:
        mobirevi = i.text
        review.append(mobirevi)
    print(len(review))


df = pd.DataFrame({"Names": Name, "Prices": Prices, "Description": description, "Reviews": review})
print(df)
df.to_csv("Mobile Data.csv")

#link = soup.find_all("a", class_="ge-49M")

# for i in link:
#     np = i.get("href")
#     clinks = "https://www.flipkart.com" + np
#     print(clinks)
