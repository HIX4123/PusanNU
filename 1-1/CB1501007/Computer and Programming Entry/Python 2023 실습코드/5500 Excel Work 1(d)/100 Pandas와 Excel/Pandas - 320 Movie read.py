#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('movies.xls', sheet_name='1900s')

print("Column headings:")
print(df.columns)

print(df['Actor 1'])

print(df[df.columns[6]])


print("감독")
for i in df.index:
    print(df[df.columns[10]][i])


Genres      = df['Genres']
Country     = df['Country']
IMDB_Score  = df['IMDB Score']

for i in Country.index:
    print( Country[i])