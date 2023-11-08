#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-01
#-------------------------------------------------------------------------------




# import libraries
import numpy as np
import pandas as pd
import os

# set directory with yours
base_dir = 'D:/admin/Documents'
excel_file = 'sales_per_region.xlsx'
excel_dir = os.path.join(base_dir, excel_file)

# read a excel file and make it as a DataFrame
df_from_excel = pd.read_excel(excel_dir, # write your directory here
                             sheet_name = 'Sheet1',
                             header = 2,
                             #names = ['region', 'sales_representative', 'sales_amount'],
                              dtype = {'region': str,
                                         'sales_representative': np.int64,
                                         'sales_amount': float}, # dictionary type
                              index_col = 'id',
                              na_values = 'NaN',
                              thousands = ',',
                              nrows = 10,
                              comment = '#')

#