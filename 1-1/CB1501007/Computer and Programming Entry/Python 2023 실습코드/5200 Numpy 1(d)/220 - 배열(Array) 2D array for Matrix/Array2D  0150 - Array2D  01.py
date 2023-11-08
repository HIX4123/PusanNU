

import numpy as np

# array 함수를 사용하는 일반 python 리스트나 튜플을 이용
a = np.array([2,3,4])
print(("\n 배열 a = %s" %a))
print(("\n 배열 a의 각 요소의 데이터형 : %s " %a.dtype))
b = np.array([2.3, 3.3, 4.4])
print(("\n 배열 b = %s" %b))
print(("\n 배열 b의 각 요소의 데이터형 : %s " %b.dtype))
c = np.array([(1.5, 2, 3), (4, 5, 6)])
print("\n 배열 C는 2차원 배열 : ")
print(c)

print("\n\n 배열을 생성할 때, 요소들은 모르고 크기만 지정하고 싶은 경우")
print("\n 0으로 가득찬 배열 만들기")
print((np.zeros((3,4))))
print("\n 1으로 가득찬 배열 만들기")
print((np.ones((2,5))))

print("\n 랜덤값을 가지는 배열 만들기")
print((np.random.random((4,4))))
