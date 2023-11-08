#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-20
#-------------------------------------------------------------------------------


import random
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2020)

a1 = np.random.choice(5, 5, replace=False)  # shuffle 명령과 같다.
a2 = np.random.choice(10, 3, replace=False)  # 3개만 선택
a3 = np.random.choice(7, 10)  # 반복해서 10개 선택
a4 = np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0])  # 선택 확률을 다르게 해서 10개 선택


L=[a1, a2, a3, a4 ]
for w in L :
    print(w)
