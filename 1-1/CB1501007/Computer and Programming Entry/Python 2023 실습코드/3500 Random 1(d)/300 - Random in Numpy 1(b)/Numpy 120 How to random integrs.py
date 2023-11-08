#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-20
#-------------------------------------------------------------------------------


import random
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2020)

ar0 = np.random.rand(10, 3 )  # 3차원 표준점 10개
ar1 = np.random.randint(   6, size=10)  #0에서 5까지의 점 10개
ar2 = np.random.randint(  30, size= 5)
ar3 = np.random.randint(1000, size=(10, 2)) # 1000범위의 점, 10개, 차원은 2차원

# Generate a 2 x 4 array of ints between 0 and 4, inclusive:
ar4 = np.random.randint(100,500, size=(10, 2))

L = [ar0, ar1, ar2, ar3, ar4 ]

for (i,w) in enumerate(L) :
    print(i, "=")
    print( w)


