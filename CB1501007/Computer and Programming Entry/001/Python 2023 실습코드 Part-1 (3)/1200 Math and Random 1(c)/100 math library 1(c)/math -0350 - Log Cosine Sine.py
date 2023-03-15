


import math # 수학에 관련된 함수를 하기 위해서는 반드시 먼저 불러야 한다.
             # 이것을 python module(모듈)이라고 한다.
# from math sqrt, pi 로 하면 좀 "가벼운" 모듈을 만들 수 있다.



print("\n Floor function =",   math.floor( 45.4/ 12.2))
print("\n Celiing function =", math.ceil ( 45.4/ 12.2))

print("\n 다양한 Log 함수", math.log(1024,2), math.log(10.2), math.log10(100000))

print("\n 다양한 삼각 함수", math.sin( math.pi/2), math.cos( math.pi/3))




print(__name__)  #특별한 변수 __name__ 는 사용된 module을 지시해준다.