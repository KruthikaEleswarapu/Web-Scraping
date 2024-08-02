from bs4 import BeautifulSoup
import requests
import pandas as pd


Name=[]
Price=[]
Review=[]
Desc=[]

for i in range(1,11):
    url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_="_4rR01T")
    for i in names:
        n=i.text
        Name.append(n)

    price=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in price:
        n=i.text
        Price.append(n)

    desc=box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        n=i.text
        Desc.append(n)       

    reviews=box.find_all("div",class_="_3LWZlK")
    for i in reviews:
        n=i.text
        Review.append(n)

df=pd.DataFrame({"Name":Name,"Price":Price,"Desc":Desc,"Review":Review})
df.to_csv('Mobiles.csv')
print(df)