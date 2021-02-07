import requests
from bs4 import BeautifulSoup
import pandas as pd
response= requests.get("https://www.imdb.com/chart/top")
#print(response)
html_içeriği=response.content
soup= BeautifulSoup(html_içeriği,"html.parser")
titles=soup.find_all("td",{"class":"titleColumn"})
ranking=soup.find_all("td",{"class":"ratingColumn imdbRating"})
ratingg=list()
title=list()
for baslik, rating in zip(titles,ranking):   
    baslik = baslik.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    baslik=baslik[8:]
    title.append(baslik)
    rating = rating.text
    rating = rating.strip()
    rating = rating.replace("\n","")
    ratingg.append(rating)

d={"Film İsmi":title, "Rating":rating}
data=pd.DataFrame(d)
print(data)
data.to_csv("imbd.csv")
