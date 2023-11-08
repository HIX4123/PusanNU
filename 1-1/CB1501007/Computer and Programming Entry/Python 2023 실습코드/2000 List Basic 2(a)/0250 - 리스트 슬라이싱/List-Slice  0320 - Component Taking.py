#--------------------------------------------------------
# Author:      Zoh Que
# Created:     21-02-2023
#--------------------------------------------------------

import numpy as np

L = [ [1,2], [3,4], [5,6], [7,8], [9,10], [-2, -3], [0,99]]

A = np.array(L)

print(A)

L1= A[:,0]      # 첫번째 component
print(f"L1={L1}")

L2= A[:,1]
print(f"L2={L2}")