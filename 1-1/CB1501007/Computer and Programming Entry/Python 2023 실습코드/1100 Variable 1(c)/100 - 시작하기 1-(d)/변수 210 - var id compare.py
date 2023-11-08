
# system의 내부를 살펴보기
import sys

a = 500
c = 500
print(id(a))  # 내부에서 구분되는 이름이다.
b = a
print(id(b))   # 수행할 때마다 조금씩 다른 장소에 배치된다.
print(a is b)
print(a is c)
print(b is c)
print(a == b)

print("실험 2")
p = [1,2,3]
q = [1,2,3]

print(id(p), id(q), p is q, p == q)  # 리스트는 정수와 다르다.
