#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd

data1 = pd.read_excel ('Interfood.xlsx',  sheet_name="Korea")


df = pd.DataFrame(data1, columns= ['이름','가격'])
print (df)

cname =  df.columns.ravel()
data2 = pd.read_excel ('Interfood.xlsx',  sheet_name="Japan")
df = pd.DataFrame(data2, columns= ['이름','가격'])

print(" 1> ", df['이름'] )
print(" 2> ", df['가격'] )
print(" 3> ", df['이름'][2] )
print(" 4> ", df['가격'][1] )

for w in   df['이름'] :
    print(f' df["이름"]={w}')