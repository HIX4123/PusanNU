
import numpy as np
from   numpy import poly1d

Poly= [ poly1d([ 1, 0, 1]),  # x^2+1
        poly1d([ 1,-2,-1]),
        poly1d([-1, 0, 0,-1]),
        poly1d([ 1, 1, 0,-1]),
        poly1d([-1, 1, 1,-1]),
        poly1d([-1, 0, 0, 1,-1]),
        poly1d([ 1, 1, 2,-1,-1]),
        poly1d([ 1, 0, 1,-1, 2, -1]),
         ]


B = poly1d([1])  # B[x]=1

for w in Poly :
    B *= w
    print(B.c)


