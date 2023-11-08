

import numpy

la = numpy.arange(50)
lb = la.reshape(5,10) # 과학계산에서 매우 매우 중요한 작업
print("la= ", la)
print("lb= ", lb)


print("lb[0,1]=", lb[0][1])
print("lb[2,5]=", lb[2][5])
print("lb[3,2]=", lb[3][2])
print("lb[4,0]=", lb[4][0])

import numpy as np

a = np.arange(12)
print("\n a=\n", a)
b = a.reshape(3, 4)
print("\n b=\n",b)

# 사용하는 원소의 갯수가 정해저 있기 때문에 reshape 명령의
# 형태 튜플의 원소 중 하나는 -1이라는 숫자로 대체할 수 있다.
# -1을 넣으면 해당 숫자는 다를 값에서 계산되어 사용된다.

c= a.reshape(3, -1)
print("c=\n", c)

d = a.reshape(2, 2, -1)
print("d=\n", d)

e = a.reshape(2, -1, 2)
print("e=\n", e)


# 다차원 배열을 무조건 1차원으로 펼치기 위해서는 flatten 명령이나
# 메서드를 사용한다.

f = a.flatten()
print("f=\n", f)


# 배열 사용에서 주의할 점은 길이가 5인 1차원 배열과 행,
# 열의 갯수가 (5,1)인 2차원 배열 또는 행, 열의 갯수가 (1, 5)인
# 2차원 배열은 데이터가 같아도 엄연히 다른 객체라는 점이다.

x = np.arange(5)
y = x.reshape(1, 5)
z = x.reshape(5, 1)

print("-----------------\n")
print("x=\n", x)
print("y=\n", y)
print("z=\n", z)


# 이렇게 같은 배열에 대해 차원만 1차원 증가시키는 경우에는
# newaxis 명령을 사용하기도 한다.



print(x[:, np.newaxis])


