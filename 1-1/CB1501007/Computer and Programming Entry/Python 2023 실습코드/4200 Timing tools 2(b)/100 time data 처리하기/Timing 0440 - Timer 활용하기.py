"""
파이썬에서는 timeit 모듈을 사용하여 특정 프로젝트의 전체
실행시간이 아닌 특정 함수나 코드의 실행시간을 측한다.

timeit.timeit()
timeit.timeit(stmt='pass',
              setup='pass',
              timer=<default timer>,
              number=1000000,
              globals=None)

timeit 함수의 파라미터는 아래와 같습니다.

    stmt: 실행측정할 코드 및 함수
    setup: stmt를 실행하기 위해 사전에 필요한 코드나 함수를 선언.
    setup의 실행 시간은 전체 측정 실행 시간에서 제외됨
    timer: Timer 인스턴스
    number: 선언한 stmt의 수행 횟수.
    선언하지 않으면 기본값으로 1000000번이 실행됨
    """


import timeit

runthis= """
D=[]
for w in range(100000):
    D.append(w)
"""

t1 = timeit.timeit( runthis, number=10)
print(f"time for run this= {t1:12.7}")


runthat= """
D=[]
for w in range(100000):
    D.insert(0,w)
"""


t1 = timeit.timeit( runthat, number=10)
print(f"time for run that= {t1:12.7}")