#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-01
#-------------------------------------------------------------------------------



import pandas

xls = pandas.ExcelFile ('3tabs.xlsx')
print( "All Sheet Names=", xls.sheet_names )

excel_2 = pandas.read_excel('3tabs.xlsx', sheet_name='region')
print(excel_2)
print(excel_2.columns.ravel())
print(excel_2['지역'].tolist())

print("\n\n 다른 sheet")
excel_3 = pandas.read_excel('3tabs.xlsx', sheet_name='baseball')
print(excel_3)
print(excel_3.columns.ravel())
print(excel_3['타율'].tolist())