#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd

df = pd.read_excel ( 'Interfood.xlsx', sheet_name="Italy",header= None )

print(df)

