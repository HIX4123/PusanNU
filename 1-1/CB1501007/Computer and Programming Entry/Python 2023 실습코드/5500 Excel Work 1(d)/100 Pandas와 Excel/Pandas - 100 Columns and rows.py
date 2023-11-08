#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

# 반드시 먼저 미리 설치되어야할 package
# 1) pandas
# 2) openpyxl

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('interfood.xlsx', sheet_name='Korea')

print("Column headings:")
print(df.columns)
colname = df.columns.tolist()

Kname     = df['이름']
Kprice    = df['가격']
Kgood     = df['건강']

for i in Kname.index:
    print( f'{i}= {Kname[i]}')

for i in Kprice.index:
    print( f'{i}= {Kprice[i]}')

cname =  df.columns.ravel()
print( df[ cname[2] ].tolist() ) # list로 만들기


print("row length=", len(cname) )
print("column length=", len(df) )

for colnum in range( df.shape[0] ) :
    print("\n")
    for rownum in range( df.shape[1] ) :
        print( f'{df.iloc[ colnum, rownum]:10}', end= " " )