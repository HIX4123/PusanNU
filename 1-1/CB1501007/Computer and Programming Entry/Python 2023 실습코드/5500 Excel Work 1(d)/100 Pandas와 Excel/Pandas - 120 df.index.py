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

print("df.index=", df.index )


for w in range(df.index.start):
    print(w)