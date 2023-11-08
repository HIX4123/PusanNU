#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-29
#-------------------------------------------------------------------------------

import pandas as pd
df = pd.read_csv('3tabs.csv')

print("Column headings:")
print(df.columns)

print("\n df=name ")

print(df['나라'])

print(df[df.columns[2]])