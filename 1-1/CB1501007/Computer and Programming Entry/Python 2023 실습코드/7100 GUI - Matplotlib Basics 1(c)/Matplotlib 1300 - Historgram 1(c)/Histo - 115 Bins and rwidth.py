#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(1000)

counts, bins, patches = plt.hist(y, 12, rwidth=0.8) # histogram을 12개로 나눈다.

print("n=", counts )
print("sum(n)=", sum( counts ))
print("bins=", bins)

plt.show()