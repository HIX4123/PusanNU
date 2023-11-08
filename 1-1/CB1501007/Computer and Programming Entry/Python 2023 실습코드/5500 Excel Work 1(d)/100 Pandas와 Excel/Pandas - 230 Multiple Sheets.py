#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-01
#-------------------------------------------------------------------------------

import pandas as pd

excel_file = 'movies.xls'
xlsx = pd.ExcelFile(excel_file)

print( xlsx.sheet_names )

movies_sheets = []
for sheet in xlsx.sheet_names:
   movies_sheets.append(xlsx.parse(sheet))


movies = pd.concat(movies_sheets)