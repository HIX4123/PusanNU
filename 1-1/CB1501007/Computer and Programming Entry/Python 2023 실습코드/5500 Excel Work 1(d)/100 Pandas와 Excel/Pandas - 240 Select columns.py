#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

# 여기로 보세요. https://pbpython.com/excel-pandas-comp.html

import pandas as pd
import numpy as np
df = pd.read_excel("excel-comp-data.xlsx")
print( df.head() )

df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
print( df.head() )

# 각 칼럼의 sum 을 구하기

print( df["Jan"].sum(), df["Jan"].mean(),df["Jan"].min(),df["Jan"].max())

sum_row=df[["Jan","Feb","Mar","total"]].sum()
print( "sum_row=\n", sum_row )

# transpose로 돌리기
df_sum=pd.DataFrame(data=sum_row).T
print( df_sum )

# append로 추가하기
df_final=df.append(df_sum,ignore_index=True)
print( df_final.tail() )