


import math # 수학에 관련된 함수를 하기 위해서는 반드시 먼저 불러야 한다.
             # 이것을 python module(모듈)이라고 한다.
# from math sqrt, pi 로 하면 좀 "가벼운" 모듈을 만들 수 있다.


coff =[ (3,4), (-2,1), (5,1), (-3, -2)]
my = 1
for w in coff :
    a=w[0]
    b=w[1]
    my = my + complex(a,b)
    print(my)




print(__name__)  #특별한 변수 __name__ 는 사용된 module을 지시해준다.