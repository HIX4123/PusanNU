#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-06-01
#-------------------------------------------------------------------------------

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.min_weight_full_bipartite_matching.html#scipy.sparse.csgraph.min_weight_full_bipartite_matching

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import min_weight_full_bipartite_matching

print("min_weight_full_bipartite_matching ")
biadjacency_matrix = csr_matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
print(min_weight_full_bipartite_matching(biadjacency_matrix)[1])

from scipy.sparse.csgraph import maximum_bipartite_matching
print("maximum_bipartite_matching ")
biadjacency = csr_matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
print(maximum_bipartite_matching(biadjacency, perm_type='column'))

# When multiple edges are available, the ones with lowest weights are preferred:
print("multiple edges are available ...")
biadjacency = csr_matrix([[3, 3, 6], [4, 3, 5], [10, 1, 8]])
row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
print(col_ind)

# The total weight in this case is

print(biadjacency[row_ind, col_ind].sum())