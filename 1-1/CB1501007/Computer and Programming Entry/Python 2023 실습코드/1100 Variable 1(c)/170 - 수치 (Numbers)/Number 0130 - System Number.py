

import sys
import decimal

print("최대 처리 정수는 =", sys.maxsize)

a , b, c = 9, 10, 11

print(a)  ; print(b)
print(b, end=';  ') ; print(c)   # ,  콤마의 의미가 뭔가요 ?

f1, f2, f3 = 31.14e-8, 0.0000000001, 12345678901234567890.10398013012930
print(f1, f2, f3)

n = 123456789012345678901234567890987654321
m = 123456789012345678901234567890987654321  #끝에 L을 붙임

print(n)
print(m)
print("\n big number n*m = ", n*m)

# 작은 크기의 실수를 사용하면 안되는 이유, 수치오류가 발생한다.
delta= 0.00003
S = 0
for k in range(100000):
    S += delta

print("\n Final S = ", S)
if S == 3.0 : print("오차가 없음")
else : print("Oh! 오차가 있네요")

a= 34.5  # 지수계산
e=12
f=32.56
result = a**e
print("34**12승 = ", result)


