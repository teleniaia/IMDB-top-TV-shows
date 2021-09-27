import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import itertools

page = requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250') # Getting page HTML through request
soup = BeautifulSoup(page.text, 'html.parser') # Parsing content using beautifulsoup
 
links1 = soup.select("table tbody tr td.titleColumn a")
links2 = soup.select("table tbody tr td.titleColumn span")
links3 = soup.select("table tbody tr td.ratingColumn.imdbRating strong")

first10 = [(links1[:10])+(links2[:10])+(links3[:10])] # Keep only the first 10 anchors


Title = 'links1'
Year = 'links2'
Rating = 'links3'
Columns = Title, Year, Rating

for anchor in links1:
    links1=anchor.text
for anchor in links2:
    links2=anchor.text
for anchor in links3:
    links3=anchor.text

links1_dict = {'Title':links1}
links2_dict = {'Year' :links2}
links3_dict = {'Rating' :links3}

my_dict = {'Title':links1, 'Year':links2, 'Rating':links3}

df = pd.DataFrame([my_dict])

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df.head

print(df)



    

    
