
import math
import numpy as np

def parapoint(A,B,t):
    Q= t*A + (1-t)*B
    return Q

a = np.array([ 5,  9, -13])
b = np.array([-5, 11,   7])

t=0.0
while(t < 1):
    c= parapoint(a,b, t)
    print( ("t= %.3f")%t, end=" ")
    print("point=", c)
    t += 0.1