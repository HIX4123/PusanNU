import matplotlib.pyplot as plt
from numpy.random import normal

gaussian_numbers = normal(size=1000)
counts, bins, bars = plt.hist(gaussian_numbers, bins=10, rwidth=0.8 )

print( gaussian_numbers )
print(counts, bins, bars)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.hist(gaussian_numbers, bins=20, cumulative=True, rwidth=0.9)

plt.show()
