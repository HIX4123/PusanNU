#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-05-03
#-------------------------------------------------------------------------------

#
# https://brownbears.tistory.com/456
# 기본이 100만번 해당 함수를 수행한 시간을 계산해준다.
"""
timeit.repeat(stmt='pass', setup='pass', timer=<default timer>,
              repeat=5, number=1000000, globals=None)

repeat함수는 repeat 파라미터를 제외하고 timeit함수와 동일한 파라미터를
갖고 있습니다.

    stmt: 실행측정할 코드 및 함수
    setup: stmt를 실행하기 위해 사전에 필요한 코드나 함수를 선언.
    setup의 실행 시간은 전체 측정 실행 시간에서 제외됨
    timer: Timer 인스턴스
    number: 선언한 stmt의 수행 횟수. 선언하지 않으면 기본값으로
    1000000번이 실행됨
    repeat: timeit()함수를 반복으로 호출 할 수. 선언하지 않으면
    기본값으로 5번이 실행


repeat()은 결과가 repeat 파라미터에서 지정한 수만큼의 크기를 갖는
리스트를 반환합니다.
repeat() 함수는 파라미터에서 지정한 내용대로 반복하여 결과를 리스트로
내보내 줍니다. 실행시간은 측정할 때마다 동일하지 않고 계속 다르기 때문에 repeat()을 사용하여 평균 측정시간을 낼 때 사용하기 좋습니다.

"""
import timeit



def test():
    return "-".join(str(n) for n in range(100))

t1 = timeit.repeat('test()', setup='from __main__ import test', number=1, repeat=10)
for i,w in enumerate(t1) :
    print(f"{i:3}, time={w:12.8}")

print("\n 2번만 해보기 ")
t1 = timeit.repeat('test()', setup='from __main__ import test', number=10000, repeat=2)
for i,w in enumerate(t1) :
    print(f"{i:3}, time={w:12.8}")



