
import numpy as np
import matplotlib.pyplot as plt

mean = (1, 2)
cov = [[1, 0], [0, 1]]
x = np.random.multivariate_normal(mean, cov, (3, 3)) # [x,y]가 3 by 3 행렬로 생성

print(x)

print("x.shape=", x.shape)

# The following is probably true, given that 0.6 is roughly twice the standard deviation:


print(list((x[0,0,:] - mean) < 0.6))

