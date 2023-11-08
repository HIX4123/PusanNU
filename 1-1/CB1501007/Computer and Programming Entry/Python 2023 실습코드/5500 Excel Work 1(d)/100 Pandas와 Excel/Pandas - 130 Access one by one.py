#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('interfood.xlsx', sheet_name='Korea')

print("Column headings:")
print(df.columns)

cname =  df.columns.ravel()


print("row length=", cname, len(cname) )
print("column length=", len(df) )

for w in cname :
    print( f'{w}------\n{df[w]}')
    print( df[w].tolist() )