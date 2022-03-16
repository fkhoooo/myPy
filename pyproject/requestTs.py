from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
# for child in bsObj.find("table",{"id":"giftList"}).children:
#  print(child)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList: 
 print(name.get_text())