
import numpy as np
import matplotlib.pyplot as plt
A = np.random.standard_normal(( 50, 2))
A += np.array((-1, -1))
B = np.random.standard_normal(( 50, 2))
B += np.array((1, 1))

print(A)
print(B)

plt.scatter(B[:,0], B[:,1], c = 'k', s = 100., alpha=0.3 )
plt.scatter(A[:,0], A[:,1], c = 'r', s = 75., alpha=0.4 )

plt.show()