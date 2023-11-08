#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-29
#-------------------------------------------------------------------------------

# csv를 저장할 때는 반드시 unicode/utf-8로 저장해야 함.


import pandas as pd
df = pd.read_csv('mdata.csv')
print(df)


df.to_csv('mdata02.csv')

