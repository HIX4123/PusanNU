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