#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-20
#-------------------------------------------------------------------------------


import random
import numpy as np

ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
br = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


for i,w in enumerate(ar) :
    print(f"i={i}, w={w}")


print(ar+br)
print(ar-br)
print(ar*br)
print(ar/br)
print(ar**br)


