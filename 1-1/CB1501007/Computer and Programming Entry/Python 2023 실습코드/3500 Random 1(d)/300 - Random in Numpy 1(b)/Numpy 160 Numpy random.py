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
ar4 = np.random.randn(15) # 정규분포 점 15개 , 평균이 0, 분산1
ar5 = np.random.randn(10, 3) # 3차원 정규분포점
ar6 = np.random.randint(5, size=(10, 4))
ar7 = np.random.randint(10, 20, size=(3, 5))

L = [ar0, ar1, ar2, ar3, ar4, ar5, ar6, ar7 ]

for (i,w) in enumerate(L) :
    print("\n ar", i, "=")
    print( w)


