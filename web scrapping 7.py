import requests
import pandas as pd
from bs4 import  BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r= requests.get(url)
soup =BeautifulSoup(r.text,"html.parser")
names = (soup.find_all("a", class_="title"))
#print(names)
#product names
Product_name=[]
for i in names:
    nam=i.text
    Product_name.append(nam)

#print(Product_name)
#Product prices
prices=(soup.find_all("h4",class_="float-end price card-title pull-right"))
price_list=[]
for i in prices:
    pric= i.text
    price_list.append(pric)

#print(price_list)
#Product Description
description = (soup.find_all("p",class_="description card-text"))
description_list=[]
for i in description:
    desc = i.text
    description_list.append(desc)

#print(description_list)
#Product Reviews
reviews = (soup.find_all("p",class_="float-end review-count"))
reviews_list = []
for i in reviews:
    review = i.text
    reviews_list.append(review)

#print(reviews_list)

df = pd.DataFrame({"Products Name":Product_name,"Prices":price_list,"Description":description_list,"Reviews":reviews_list})
#print(df)
df.to_csv("Product_details .csv")