
# 튜플 선언
tup1 = (1,2,3)
tup2 = (4, 5)
tup3 = tup1 + tup2

# tuple의 크기를 변화시킨다. vector로서가 아니라.

print(tup3)   # tuple은 vector가 아니다. 그냥 뒤에 붙이는 형식
print(tup1*3)
# print(tup2/2) # 이것은 support 되지 않는다.

# 만일 원한다면 이렇게 해야 한다.

import numpy as np

v1 = np.array([3,2,1])
v2 = np.array([5,6,2])

sum_vector = v1 + v2