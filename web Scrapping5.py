import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"html.parser")
#div=(soup.find('div'))
#print(div)
#tag = (soup.find("h4",{"class":"float-end price card-title pull-right"}))
#print(tag.string)
#desc = (soup.find("p",{"class":"description card-text"}))
#print(desc.string)
#<!-- Another Method -->
#a= (soup.find("p" ,class_="description card-text"))
#print(a.string)
a = (soup.find_all("a",class_="title"))
#print(len(a))
 #j is a variable
#for j in a:
     #print(j.text)
para = (soup.find_all("p", class_="description card-text"))
#print(para)
#for i in para:
     #print(i.text)


