import requests
from bs4 import BeautifulSoup
url ="https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
#boxes = soup.find_all("div",class_ = "col-md-4 col-xl-4 col-lg-4")
#print(len(boxes))
box =soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
#print(box)
if len(box) >= 5:
    i = box[4]
#    print(i)

#print data inside a tag
#name = i.find("a").text
#print(name)
#desc = i.find("p").text
#print(desc)
navbar = soup.find_all("ul",class_="nav flex-column" ,id="side-menu")

#print(navbar)
for navb in navbar:
# Find the li element with the specified class within each ul element
 sidebr = navb.find("li", class_="nav-item active")

# Check if the sidebr element is found
print(sidebr.text)
