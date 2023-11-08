#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-06-29
#-------------------------------------------------------------------------------

# csv로 바꿀 때에는 반드시 utf-BOM이나 utf-unicode로 바꾸어야 함

import pandas

# read csv file
df = pandas.read_csv('3tabs.csv') # df is pandas.DataFrame
print("##### data #####")
print(df)

print("##### df.loc[0:1] #####")
print(df.loc[0:1])


print("##### df.loc[:, '여름온도':'겨울온도'] #####")
print(df.loc[:, '여름온도':'겨울온도'])

print("##### df.loc[[0, 2], 'name':'age'] #####")
print(df.loc[[0, 2], '지역':'겨울온도'])

##print("##### df.loc[:, 'name'] #####")
##print(df.loc[:, 'name'])
##
##
### final_df = df.append({'id': 4, 'name': '마루치', 'age': 14}, ignore_index=True) # 아래 두 줄과 동일한 결과를 가짐
##new_df = pandas.DataFrame([{'id': 4, 'name': '마루치', 'age': 12}])
##final_df = pandas.concat([df, new_df], ignore_index=True)
##print(final_df)
##
##final_df.to_csv('new_output.csv', index=False, header=False, \
##                columns=['id', 'name', 'age'])


