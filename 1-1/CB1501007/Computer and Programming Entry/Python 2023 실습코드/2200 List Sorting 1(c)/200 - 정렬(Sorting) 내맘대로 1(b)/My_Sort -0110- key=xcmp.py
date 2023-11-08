#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-03-28
#-------------------------------------------------------------------------------
from functools import cmp_to_key

Ln= ["개똥", "다람쥐나무", "콩나물", "부대찌게", "곰통", "밥"]


def xcmp(w):
    return( len(w) )

L1 = sorted( Ln, key = xcmp )
print(L1)


L1 = sorted( Ln, key = len )
print(L1)