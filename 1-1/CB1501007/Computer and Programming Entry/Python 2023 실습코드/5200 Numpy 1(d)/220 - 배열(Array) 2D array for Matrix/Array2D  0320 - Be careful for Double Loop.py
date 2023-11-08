
import numpy

def printM( X):
    for A in X :
         print("\n")
         for b in A :
            print(b, end=' ')

n = 5
m = 6
a = [[0] * m] * n
a[0][0] = 25
a[1][2] = -3


printM(a)
