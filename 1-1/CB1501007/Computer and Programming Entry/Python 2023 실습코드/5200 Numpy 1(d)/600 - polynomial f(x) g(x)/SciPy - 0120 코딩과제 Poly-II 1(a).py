
import numpy as np
from   numpy import poly1d


f = poly1d([1,0,0,-1,1,-2,1])  # p(x)=x^6 - x^4 ...
g = poly1d([1,-2,0,1,0,0,0,-3])
h = poly1d([1,0,1])
print(f, g, h)
Q = f*g*h

print("\n Q(x)= \n", Q )


print( "Q(2)=", Q(2))  # 값 계산
print( "Q.c=", Q.c)
print( "Q.c의 type=", type(Q.c))

for w in f.r :
    print( "root of f(x)=", w )

for w in h.r :
    print( "root of h(x)=", w )



