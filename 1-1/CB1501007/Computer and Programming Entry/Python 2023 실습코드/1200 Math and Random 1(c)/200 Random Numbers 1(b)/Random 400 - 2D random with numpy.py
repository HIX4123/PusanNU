import numpy as np
import matplotlib.pyplot as plot

plot.figure(figsize=(6,6))  # 그림을 크기를 결정, 단위는 인치

N       = 10
Upper   = 500
np.random.seed(20230223)

points = np.random.randint(0,Upper,(N,2)) # N개의 원소를 2차원으로 만들어라.'

for i,w in enumerate(points) :
    print(f" {i+1:3},  ( {w[0]:3},{w[1]:3} )")

xp = list( points[:,0])     # 첫번째(0) 칼럼
yp = list( points[:,1])     # 두번째(1) 칼럼

plot.scatter(xp, yp, s=100, color="green", alpha=0.3)
plot.show()