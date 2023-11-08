
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 1000, 30 # mean and standard deviation
x = np.random.normal(mu, sigma, 100)
y = np.random.normal(mu, sigma, 100)

for p in zip(x,y) :
    print(p)
