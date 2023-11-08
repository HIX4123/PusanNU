"""
timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=5, number=1000000, globals=None)
repeat함수는 repeat 파라미터를 제외하고 timeit함수와 동일한 파라미터를 갖고 있습니다.

stmt: 실행측정할 코드 및 함수
setup: stmt를 실행하기 위해 사전에 필요한 코드나 함수를 선언. setup의 실행 시간은 전체 측정 실행 시간에서 제외됨
timer: Timer 인스턴스
number: 선언한 stmt의 수행 횟수. 선언하지 않으면 기본값으로 1000000번이 실행됨
repeat: timeit()함수를 반복으로 호출 할 수. 선언하지 않으면 기본값으로 5번이 실행
"""

import timeit
import random


def make_list(N):
    L=[ random.random() for i in range(1,N) ]
    return(L)

# 반드시 setup에서 사용할 함수를 미리 선언해야 한다.
X = timeit.timeit( stmt="make_list(10000)", setup='from __main__ import make_list',  number = 1000 )
print(X)


def Lsort():
    global X
    X.sort()

for w in [10,100,1000,10000,100000] :
    N = w
    X=[ random.random() for i in range(1,N) ]
    print( "N=", N, ":  ", timeit.timeit(stmt="Lsort()", setup='from __main__ import Lsort', number=N) )





