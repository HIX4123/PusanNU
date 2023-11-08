

import numpy as np

print("\n test02 - 2차원 배열(4행 3열)")
array2 = np.arange(4*3).reshape(4,3)
print(array2)

print("\n test03 - 3차원 배열(높이가 3인 2행 4열 배열 = 2행 4열 배열 3개)")
array3 = np.arange(3*2*4).reshape(3, 2, 4)
print(array3)

print("\n test04 - 만약 배열의 크기가 너무 커서, 다 표시될 수 없으면 \
        자동으로 배열의 중간 값들을 생략한다.")
print((np.arange(10000).reshape(100,100)))

print("대각 행렬 생성하기")
x = np.eye(10)
print(x)
print("x[3][5]=" , x[3][5])