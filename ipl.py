import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.iplt20.com/auction"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
tables=soup.find_all("table",class_="ih-td-tab auction-tbl")
#print(tables.text)
rows=soup.find_all("tr")
for i in rows:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()#to remove all the blanks due to image
    #data,first_td=i.find_all("td")[0].find("h2",class_="ih-pt-cont").text.strip()
    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0,first_td)
df=pd.DataFrame(columns=row)
df.to_csv("IPL.csv")
