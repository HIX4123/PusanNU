#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd

df = pd.read_excel ( 'Interfood.xlsx', sheet_name="Italy" )

cname =  df.columns.ravel()
# ['이름' '재료' '부재료']

print("\n Column=", cname[2])
print("tolist=", df[ cname[2] ].tolist())



df = pd.read_excel ( 'Interfood.xlsx', sheet_name="Italy" , \
                      usecols=['이름', '부재료'])
print(df)

