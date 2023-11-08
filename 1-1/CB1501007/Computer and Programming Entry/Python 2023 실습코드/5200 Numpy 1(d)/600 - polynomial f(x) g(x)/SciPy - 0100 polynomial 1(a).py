
import numpy as np
from numpy import poly1d


p = poly1d([3,4,5])  # p(x)=3x^2 + 4x + 5
print("p(x)= \n", p)

print("\n (p(x)+1)p(x)= \n", (p+1)*p)
print("\n 적분 p(k=6)= \n", p.integ(k=6))
print("\n 미분 p'(x)= \n", p.deriv())
print("\n eval p(1), p(-1)= ", p([1, -1]))   # p(1), p(-1)


print("\n p(x)^2 / p(x)-5 = \n", p*p/(p-5))
# asarray(p) gives the coefficient array, so
# polynomials can be used in all functions that accept arrays:




