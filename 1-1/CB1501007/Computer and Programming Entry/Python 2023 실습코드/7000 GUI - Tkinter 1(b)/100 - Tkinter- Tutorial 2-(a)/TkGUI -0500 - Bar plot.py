# !/usr/bin/python3
import matplotlib.pyplot as plt
from numpy.random import normal

gaussian_numbers = normal(size=1000)
plt.hist(gaussian_numbers, bins=10, rwidth=0.8 )
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
