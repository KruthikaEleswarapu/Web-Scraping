import requests 
from bs4 import BeautifulSoup
import pandas as pd

url= 'c:\https:\\ticker.finology.in\market'
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")

