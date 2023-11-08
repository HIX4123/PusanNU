#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-29
#-------------------------------------------------------------------------------

# csv로 바꿀 때에는 반드시 utf-BOM이나 utf-unicode로 바꾸어야 함

import pandas

df = pandas.read_csv('3tabs.csv') # df is pandas.DataFrame
print("##### df = 3tabs.csv #####")
print(df)

print("##### df.loc[0:1] #####")
print(df.loc[0:1])


print("##### df.loc[:, '여름온도':'겨울온도'] #####")
print(df.loc[:, '여름온도':'겨울온도'])

print("##### df.loc[[0, 2], 'name':'age'] #####")
print(df.loc[[0, 2], '지역':'겨울온도'])

print("##### df.loc[:, '나라'] #####")
print(df.loc[:, '나라'])

final_df = df.append({'지역':'제주도', '여름온도':29.12, '나라':'탐라국'}, ignore_index=True) # 아래 두 줄과 동일한 결과를 가짐
print(final_df)
##
##final_df.to_csv('new_output.csv', index=False, header=False, \
##                columns=['id', 'name', 'age'])






