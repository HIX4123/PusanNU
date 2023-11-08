#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------

#!/usr/bin/python3

import openpyxl

book = openpyxl.load_workbook('Ball.xlsx')

sheet = book.active

cells = sheet['A1': 'C10']

for c1, c2, c3 in cells:
    print("{0:8}  {1:8}  {0:3}".format(c1.value, c2.value, c3.value))