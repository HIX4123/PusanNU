import numpy as np

L = [
  [1,2,3],
  [9,1,4],
  [7,7,2],
  [6,3,4],
  [1,0,0],
  [5,3,8]
]


print(L)
NL = np.array(L)
print(NL)
print(NL[:,0])

X = np.array(L)[:,1]
print(X)