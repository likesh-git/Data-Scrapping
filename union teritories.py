wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

import requests

source = requests.get(wiki).text

from bs4 import BeautifulSoup



soup = BeautifulSoup(source, "lxml")


state_table = soup.find('table', class_ = "wikitable")

A = []
B = []
C = []
D = []
E = []
F = []



for row in state_table.findAll('tr'):
   tdlist = row.findAll('td')
   thlist = row.findAll('th')
    
   if (len(row.findAll('td')) == 6):
        #scrapper code
        A.append(thlist[0].text.strip())
        B.append(tdlist[1].text.strip())
        C.append(tdlist[2].text.strip())
        D.append(tdlist[3].text.strip())
        E.append(tdlist[4].text.strip())
        F.append(tdlist[5].text.strip())
        
        
import pandas as pd

df = pd.DataFrame()

df['State'] = A
df['AdminCap'] = B
df['LegisCap'] = C
df['JudiCap'] = D
df['Year'] = E
df['FormerCap'] = F


df.to_csv('states.csv', index = False)

#read into a df
#make changes in df
#save back to csv

#----------------------------
#databases

#saving the df to sqlite3 database

import sqlite3 as sqldb

conn  = sqldb.connect('states.db')

df.to_sql('statetable', conn, index = False)


#------
#read the data from database

rconn = sqldb.connect('states.db')

new_df = pd.read_sql('SELECT * FROM statetable ' , rconn)

#------------
#cursor concept

fconn = sqldb.connect('states.db')

mycursor = fconn.cursor()

mycursor.execute('SELECT * FROM statetable')

for record in mycursor:
    print (record[0])
    
    
    
#pymongo





        
        
       


