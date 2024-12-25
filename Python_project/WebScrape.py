import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np

r = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(r.content, 'html.parser') 
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
df = df[0]
print(df)