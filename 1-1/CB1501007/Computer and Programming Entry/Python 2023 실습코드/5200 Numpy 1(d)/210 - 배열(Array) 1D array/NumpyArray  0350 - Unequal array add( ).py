#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-26
#-------------------------------------------------------------------------------
import numpy as np
a = np.array([3, 2, 1])
b = np.array([1, 2])

def unequal_add(a,b):
    if len(a) < len(b):
        c = b.copy()
        c[:len(a)] += a
    else:
        c = a.copy()
        c[:len(b)] += b
    return(c)


print(unequal_add(a,b))
