#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import numpy as np

N=4 ; M=5
M = np.asarray([[(i,j) for j in range(M)] for i in range(N)] , dtype='int,int')

M[2,3]= (34,67)  #when you give coordinate position for (x,y)

print("M=", M)