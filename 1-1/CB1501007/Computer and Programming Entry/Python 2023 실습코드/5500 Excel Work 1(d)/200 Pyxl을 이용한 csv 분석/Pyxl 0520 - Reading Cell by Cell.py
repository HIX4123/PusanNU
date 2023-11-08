#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------


import openpyxl

book = openpyxl.load_workbook('Ball.xlsx')

sheet = book.active

cells = sheet['A1': 'B6']

for c1, c2 in cells:
    print("{0:8} {1:8}".format(c1.value, c2.value))