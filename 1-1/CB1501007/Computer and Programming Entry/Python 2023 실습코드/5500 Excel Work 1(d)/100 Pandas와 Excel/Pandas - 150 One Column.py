
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('movies.xls', sheet_name='2010s') # 년도 조심

print("Column headings:")
print(df.columns)

print(df['Actor 1'])

print(df[df.columns[6]])

"""
Index([
'Title',
'Year',     'Genres',       'Language', 'Country',        'Content Rating',
'Duration', 'Aspect Ratio', 'Budget',   'Gross Earnings', 'Director',
'Actor 1',  'Actor 2',      Actor 3',   'Facebook Likes - Director',
'Facebook Likes - Actor 1', 'Facebook Likes - Actor 2',
'Facebook Likes - Actor 3', 'Facebook Likes - cast Total',
'Facebook likes - Movie', 'Facenumber in posters', 'User Votes',
'Reviews by Users', 'Reviews by Crtiics', 'IMDB Score'],
dtype='object')
"""

##print("감독")
##for i in df.index:
##    print(df[df.columns[10]][i])

print("---------------")
for i in df.index:
    Genre= df[df.columns[2]][i].split("|")
    if 'Comedy' in  Genre and 'Thriller' in Genre :
        print(f" Oh! i={i+2:5} , {df[df.columns[10]][i]} ")

Genres      = df['Genres']
Country     = df['Country']
IMDB_Score  = df['IMDB Score']

##for i in Country.index:
##    print( Country[i])