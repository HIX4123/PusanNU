# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.min_weight_full_bipartite_matching.html#scipy.sparse.csgraph.min_weight_full_bipartite_matching

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import min_weight_full_bipartite_matching

# When the matrix is not square, i.e. when the two partitions have different cardinalities, the matching is as large as the smaller of the two partitions:


biadjacency = csr_matrix([[0, 1, 1], [0, 2, 3]])
row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
print("\n ans1= ", row_ind, col_ind)

biadjacency = csr_matrix([[0, 1], [3, 1], [1, 4]])
row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
print("\n ans2= ",row_ind, col_ind)

# When one or both of the partitions are empty, the matching is empty as well:
biadjacency = csr_matrix((2, 0))

row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)

print("\n ans3= ",row_ind, col_ind)