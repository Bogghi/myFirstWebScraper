''''
imoprting varius library 
requests for http
BeautifulSoup for scraping
pandas for dataframing
re for refex
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

''''
prepraing varius variable
strat_url is the web page to scrape
downloaded_hmml is the request object
soup is the beautiful soup object
regex is the re Object and cotain our regex to clean the head
'''
start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'
downloaded_html = requests.get(start_url)
soup = BeautifulSoup(downloaded_html.text, 'lxml')
regex = re.compile('_\[\w\]')

#w = writing mode r = reading mode
with open('downloaded.html','w') as file:
    file.write(soup.prettify())

#selec table.wikitable

full_table = soup.select('table.wikitable tbody')[0]
#print(full_table)

table_head = full_table.select('tr th')
#print(table_head)

table_column = []
for element in table_head:
    #print(element.text)
    column_lable = element.get_text(separator=" ", strip=True)
    column_lable = column_lable.replace(' ','_')
    column_lable = regex.sub('',column_lable)
    table_column.append(column_lable)
#print(table_column)

table_rows = full_table.select('tr')
table_data = []
for index,element in enumerate(table_rows):
    if index > 0:
        row_list = []
        value = element.select('td')
        for value in value:
            row_list.append(value.text.strip())
        table_data.append(row_list)

df = pd.DataFrame(table_data, columns=table_column)
print(df)

#print(table_data)
 