from bs4 import BeautifulSoup
import urllib.request
import sqlite3
import datetime
global str
time = datetime.datetime.now()
conn = sqlite3.connect("scarping100.db")
c = conn.cursor()
sauce = urllib.request.urlopen("https://www.bbc.co.uk/news/topics/c9qdqqkgz27t/ftse-100").read()
#sauceeuro = urllib.request.urlopen("https://www.bbc.co.uk/news/topics/cx250jmk4e7t/pound-sterling-gbp").read()

soup = BeautifulSoup(sauce, "html5lib")

for name in soup.find_all("h1",class_="topic-title gel-trafalgar-bold"):
       print(name.text)
#gets all of the divs 
for div in soup.find_all("div", class_="gel-paragon nw-c-md-market-summary__value"):
       print(div.text)



       c.execute ("INSERT INTO ftse100 (Name, Time, Value) VALUES (?, ?, ?)",
                  (name.text, time, div.text))
       conn.commit()
       c.close()
       conn.close()








