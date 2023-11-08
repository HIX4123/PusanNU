
import numpy as np
from numpy.linalg import *
"""
solve
x+2y = 5
2x+y = 4
"""

a = np.array([(1, 2), (2, 1)])
b = np.array([(5,),(4,)])

print("x, y")
print(solve(a,b))
print()

"""
solve
x+2y+3z = 1
2x+y+3z = 2
x+3y+2z = 3
"""

a = np.array([(1, 2,3), (2, 1,3),(1,3,2)])
b = np.array([(1,),(2,),(3,)])

print("x,y,z :")
print(solve(a,b))
print()


a = np.array([(1+2j, 2+1j,3-5j), (2, 1,3),(1,3,2)])
b = np.array([(1+2j,),(2-2j,),(3-1j,)])

print("Complex Number x,y,z :")
print(solve(a,b))


a = np.array([(1, 2,3,4, 5), (2, 1,3,5,4)])
b = np.array([(1,),(2,)])

#print solve(a,b)