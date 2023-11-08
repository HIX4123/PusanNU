#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import random
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0,10,size=(7, 7)), columns=list('ABCDEFG'))
print (df)

print("df.shape = ",  df.shape )

col = df.shape[0]
row = df.shape[1]

for x in range(col) :
    print("\n")
    for y in range(row) :
        print( df.iloc[x,y], end= " " )