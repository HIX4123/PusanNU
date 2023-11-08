#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd

excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)
myxlsx = pd.ExcelFile (excel_file)
print("\n Sheet 이름을 출력")
for w in myxlsx.sheet_names :
    print(w)


print(f' {movies.shape} 줄 수= {movies.shape[0]}, Column수={movies.shape[0]}')



movies_sheet1 = pd.read_excel(excel_file, index_col= 3)
print( movies_sheet1.head() )

movies_sheet1 = pd.read_excel(excel_file, sheet_name="2000s", index_col=0)
print( movies_sheet1.tail() )

movies_sheet2 = pd.read_excel(excel_file, sheet_name="2010s", index_col=0)
print( movies_sheet2.head() )