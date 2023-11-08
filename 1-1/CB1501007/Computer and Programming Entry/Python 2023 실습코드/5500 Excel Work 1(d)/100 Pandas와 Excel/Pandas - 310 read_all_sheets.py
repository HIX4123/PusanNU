#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-01
#-------------------------------------------------------------------------------


# 시작전에 반드시 > pin istall xrld 를 설치해야 한다.
# pandas도 설치

import pandas as pd


xls = pd.ExcelFile ('3tabs.xlsx')
print( "All Sheet Names=", xls.sheet_names )

df  = pd.read_excel('3tabs.xlsx', shee_tname="food")
print(df)


sheet_to_df_map = {} # to read all sheets to a map
for sheet_name in xls.sheet_names:
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)





