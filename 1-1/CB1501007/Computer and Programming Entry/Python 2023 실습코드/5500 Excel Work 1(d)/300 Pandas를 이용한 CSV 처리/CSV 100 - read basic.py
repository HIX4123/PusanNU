#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-29
#-------------------------------------------------------------------------------

import pandas as pd
df = pd.read_csv('mdata.csv')

print("Column headings:")
print(df.columns)

print("\n df=name ")

print(df['name'])

print(df[df.columns[2]])