#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)
myxlsx = pd.ExcelFile (excel_file)
print("\n Sheet 이름을 출력")
for w in myxlsx.sheet_names :
    print(w)

key="IMDB Score"
movies_sheet1 = pd.read_excel(excel_file, sheet_name="2000s", index_col=0)
sorted_by = movies.sort_values([key], ascending=False)

print("\n sorted_by_Budget \n")
print(sorted_by.head(20))
sorted_by[ key ].plot( kind="hist", rwidth=0.8 , bins=12)
plt.title(" Sorted by Movie Budget ")
plt.show()
