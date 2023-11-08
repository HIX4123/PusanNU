#-*- coding: cp949 -*-
#-------------------------------------------------------------------------------
# Purpose:     2018 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import numpy as np
a = np.array([[3,7,5],\
              [8,4,3],\
              [2,4,9]])

print '\n Our array is:'
print a


print '\n Applying amin() function:'
print np.amin(a,1)


print '\n Applying amin() function again:'
print np.amin(a,0)


print '\n Applying amax() function:'
print np.amax(a)


print '\n Applying amax() function again:'
print np.amax(a, axis = 0)