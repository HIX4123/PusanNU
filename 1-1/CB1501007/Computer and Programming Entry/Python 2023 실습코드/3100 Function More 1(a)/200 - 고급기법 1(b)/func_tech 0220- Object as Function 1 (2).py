
def applyToEach(L, f): # L은 리스트, f는 함수의 이름. 함수를 변수로  넘김.
   for i in range(len(L)):
      L[i] = f(L[i])

L = [1, -2, 3.33, 12, -6 ]

print('L =', L)
print('Apply abs to each element of L.')
applyToEach(L, abs)


print('L =', L)
print('Apply int to each element of', L)
applyToEach(L, int)

import math
def factR(N):
    return( math.factorial(N))


print('L =', L)
print('Apply factorial to each element of', L)
applyToEach(L, factR)

