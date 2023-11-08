
import numpy as np
import matplotlib.pyplot as plt
A = np.random.standard_normal(( 50, 2))
A += np.array((-1, -1))
B = np.random.standard_normal(( 50, 2))
B += np.array((1, 1))

print(A)
print(B)

plt.scatter(B[:,0], B[:,1], c = 'k', s = 100.)
plt.scatter(A[:,0], A[:,1], c = 'r', s = 25.)

plt.show()