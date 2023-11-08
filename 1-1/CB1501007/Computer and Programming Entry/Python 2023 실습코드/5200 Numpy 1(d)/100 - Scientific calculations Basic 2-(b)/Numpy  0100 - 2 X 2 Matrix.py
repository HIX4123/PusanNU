


import  numpy  as np
A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )
print("A*B=", A*B)
print("A+B=", A+B)
print( np.dot(A,B))

print("\n 단위 수의  행렬값")
a = np.array([[1, 2], \
              [3, 4]])
print("a.shape= ", a.shape)
print(np.linalg.det(a))

print("\n 2차원 점들의 3 3 by 3 행렬값")
a = np.array([ [[1, 2], [3, 4]], \
               [[1, 2], [2, 1]], \
               [[1, 3], [3, 1]] ])
print(a.shape)
print(np.linalg.det(a))

