#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-08
#-------------------------------------------------------------------------------

import numpy as np

mlist = [ 3, 5, 7, 11, 13, 22, 31, 40]



narray = np.array( mlist )
print( "narray=",  narray )

marray = narray/10
print( "marray=",  marray )

tarray = marray*2.5

for w in tarray :
    print(f'w= {w}')
