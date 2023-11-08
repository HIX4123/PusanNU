
import numpy as np

a = [11,22,33, 44, 55, 100]
print((type(a)))


# Construct an array (from a list) using np.array
b = np.array(a)
print((type(b)))

print("b[3]=", b[3])

# Or, you can skip the warm up step, directly have
c = np.array([1,2,3])
print((type(c)))

t1 = isinstance(5, int)
t2 = isinstance(a, list)
t3 = isinstance(b, np.ndarray )
print(t3)

x = isinstance("Hello", (str, float, int, list, dict, tuple))

print(x)
