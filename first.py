import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.webscraper.io/test-sites/e-commerce/allinone/phones"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
products = soup.find_all("a", class_ = "title")
product=[]
for i in products:
    name=i.text
    product.append(name)

reviews = soup.find_all("p", class_ = "review-count")
review=[]
for i in reviews:
    name=i.text
    review.append(name)

df = pd.DataFrame({"Product list":product,"Reviews":review})
df.to_excel("first.csv")