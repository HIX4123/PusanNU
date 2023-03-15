
import math  # 수학관련 작업을 하기 위해서 반드시 설치해야할 package

print ("r1 = ", math.pi)
print ("r2 = ", math.e)
print ("r3 = ", abs(-567.390923))
print ("r4 = ", int(21.567))
print ("r5 = ", math.sqrt(2))
print ("r6 = ", math.cos(0.5))
print ("r7 = ", complex(3,4))
print ("r8 = ", complex(2,-2)*complex(3,-1))
print ("r9 = ", complex(2,-2)/complex(3,-1))

a = 0x12a  # hexa
b = 0b100000
print (a,b)
print ("이진수의 표현=", bin(12356))

print ("ceiling, 천장값", math.ceil(3.001)) # math package 함수
print ("rounding, 반올림", round(3.001)  )  # 기본 내장함수

# 2차 방정식의 계수 a b c 를 사용자로 부터 입력을 받아서
# 그 해를 출력해주는 프로그램