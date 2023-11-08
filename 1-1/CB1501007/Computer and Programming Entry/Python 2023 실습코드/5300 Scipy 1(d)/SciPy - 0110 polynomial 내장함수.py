
import numpy as np
from numpy import poly1d


p = poly1d([-2,3,0,4,5])  # p(x)=3x^2 + 4x + 5

print(f" p(x)= \n {p}")
print("\n 함수의 계수(coefficient) p.c = ", p.c)

print("\n 함수의 order(최고차) p.order = ", p.order)

for w in range(p.order+1):
    print(f" {p.order-w}-차 항의 계수= {p[p.order-w]}")