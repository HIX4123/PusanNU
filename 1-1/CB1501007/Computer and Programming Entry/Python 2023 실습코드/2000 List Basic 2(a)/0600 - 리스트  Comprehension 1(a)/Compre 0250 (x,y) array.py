#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import numpy as np

alist = [[(i,j) for j in range(4)] for i in range(5)]

print("\n alist= \n", alist)

arr=np.array(alist,'i,i')  #i는 정수(integer)를 의미한다.

print("\n arr1= \n", arr)



print( type(arr[0,0]) )

blist = [ (i,j) for j in range(4) for i in range(5)]
print("\n blist= \n", blist)
