#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-06-01
#-------------------------------------------------------------------------------

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.min_weight_full_bipartite_matching.html#scipy.sparse.csgraph.min_weight_full_bipartite_matching

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import min_weight_full_bipartite_matching

# When the matrix is not square, i.e. when the two partitions have different cardinalities, the matching is as large as the smaller of the two partitions:
print(" When the matrix is not square,")

biadjacency = csr_matrix([[0, 1, 1], [0, 2, 3]])
row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
print("\n 3 by 2 Graph matched Edges", row_ind, col_ind)

biadjacency = csr_matrix([[0, 1], [3, 1], [1, 4]])
row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
print("\n 2 by 3 Graph matched Edges", row_ind, col_ind)
print(row_ind, col_ind)

print("\n  When one or both of the partitions are empty,", row_ind, col_ind)
# When one or both of the partitions are empty, the matching is empty as well:
biadjacency = csr_matrix((2, 0))
row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
print(row_ind, col_ind)