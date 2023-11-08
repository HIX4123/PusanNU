#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-13
#-------------------------------------------------------------------------------

import functools

ml = [ [1,1], [1,2], [1,3], [2,1], [2,2], [2,4],
       [3,1], [3,3], [3,4], [4,1], [4,2], [4,3] ]


def mycomp( item1, item2 ):
    d1 = item1[0]**2 + item1[1]**2
    d2 = item2[0]**2 + item2[1]**2
    if ( d1  < d2 ) : return  1
    if ( d1  > d2 ) : return -1
    if ( d1 == d2 ) : return -0  # 그대로 유지

print( "\n ml[]= \n", ml )

tl =  sorted(ml, key=functools.cmp_to_key( mycomp ) )
print( "\n tl[]= \n")
for w in tl :  print(w)