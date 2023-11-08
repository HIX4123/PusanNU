
import numpy as np
import matplotlib.pyplot as plt

maxval = 1000
N = 20


x = np.random.randint(0, maxval, N)
y = np.random.randint(0, maxval, N)

#timeit
all = np.array(list(zip(x, y)))


print( f"type(all)= {type(all)}")
for w in all :
    print(w)

plt.scatter(x, y, color="blue", alpha=0.3)
plt.show()