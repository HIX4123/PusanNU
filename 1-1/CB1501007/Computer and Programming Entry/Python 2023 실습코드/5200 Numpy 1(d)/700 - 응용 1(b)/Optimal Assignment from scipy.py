#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-06-01
#-------------------------------------------------------------------------------

import numpy as np

cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost)


print (col_ind)
print (row_ind)

#array([1, 0, 2])
print(  cost[row_ind, col_ind].sum() )

print("\n maximize version\n")
row_ind, col_ind = linear_sum_assignment(cost, maximize=True)
print (col_ind)
print (row_ind)

#array([1, 0, 2])
print(  cost[row_ind, col_ind].sum() )
