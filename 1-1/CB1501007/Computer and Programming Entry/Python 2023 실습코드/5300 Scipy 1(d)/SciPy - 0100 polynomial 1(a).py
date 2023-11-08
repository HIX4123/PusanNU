
import numpy as np
from numpy import poly1d


p = poly1d([3,4,5])  # p(x)=3x^2 + 4x + 5
print("p(x)= \n", p)

print("\n (p(x)+1)p(x)= \n", (p+1)*p)
print("\n 적분 p(k=6)= \n", p.integ(k=6))
print("\n 미분 p'(x)= \n", p.deriv())
print("\n eval p(1), p(-1)= ", p([1, -1]))   # p(1), p(-1)

# 다항식 나눗셈은 몫과 나머지, 2개를 돌려준다.
print("\n p(x)^2 / p(x)-5 = \n", p*p/(p-5))
print("\n p(x)^2 + p + 3 / p(x) = \n", (p*p+p+3)/(p))
# asarray(p) gives the coefficient array, so
# polynomials can be used in all functions that accept arrays:

print("\n 전체 poly p(x)=\n", p)
print("\n 계수만 출력하기 p.c = ", p.c)

