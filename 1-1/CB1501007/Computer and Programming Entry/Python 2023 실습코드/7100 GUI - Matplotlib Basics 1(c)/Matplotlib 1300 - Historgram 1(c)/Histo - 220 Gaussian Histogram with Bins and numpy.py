
import numpy as np
import matplotlib.pyplot as plt

arr_normal_distribution = np.random.normal(loc=0, scale=10, size=1000)
print(arr_normal_distribution)

bins = 15
plt.hist( arr_normal_distribution, bins, rwidth=0.8)
plt.title('normal distribution')
plt.show()