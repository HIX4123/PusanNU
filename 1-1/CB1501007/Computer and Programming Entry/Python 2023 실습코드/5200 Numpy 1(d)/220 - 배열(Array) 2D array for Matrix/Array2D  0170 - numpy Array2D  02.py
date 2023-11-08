

import numpy as np

print("\n arange함수를 이용해서 좀 더 간단히 배열 만들기")
print("0부터 10개")
print((np.arange(10)))
print("3부터 10-1까지의 숫자를 2 간격으로")
print((np.arange(3,10,2)))


# arange함수는 간격을 계산해서 입력해줘야 하는 단점이 있으므로
# 그럴 때에는 linspace 함수를 사용한다.

print("\n\n linspace를 이용하기")
print("0부터 2사이의 숫자를 9개")
print((np.linspace(0, 2, 9)))


print("\n\n 다차원 배열을 활용하기")
print("\n test01 - 1차원 배열 ")
array1 = np.arange(6)
print(array1)

