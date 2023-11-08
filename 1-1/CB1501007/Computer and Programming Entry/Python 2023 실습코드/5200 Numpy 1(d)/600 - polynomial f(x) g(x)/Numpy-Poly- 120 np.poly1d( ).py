import numpy as np

# Construct the polynomial x^3 + 2x - 3:
p = np.poly1d([1, 0, 2, -3])
print(np.poly1d(p))


print ( p(0.5) )

print("\n 근(roots)= ", p.r )

print("\n 근의 오차 f(root)= ", p(p.r) )


print("\n 계수= ", p.c )

print("\n 차수= ", p.order )

print("\n p[1]= ", p[2] )



# 다양한 다항식의 계산

print( "(p**3 + 4) / p = \n ", (p**3 + 4) / p )
# asarray(p) gives the coefficient array, so polynomials can be used in all functions that accept arrays:



# The variable used in the string representation of p can be modified, using the variable parameter:
p = np.poly1d([1,2,3], variable='z')
print(" np.poly1d([1,2,3], variable='z')=", p)


# Construct a polynomial from its roots:
np.poly1d([1, 2], True)


# This is the same polynomial as obtained by:
np.poly1d([1, -1]) * np.poly1d([1, -2])
