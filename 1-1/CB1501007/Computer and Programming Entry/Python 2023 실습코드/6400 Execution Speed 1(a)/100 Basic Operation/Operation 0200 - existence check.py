"""
파이썬에서는 timeit 모듈을 사용하여 특정 프로젝트의 전체
실행시간이 아닌 특정 함수나 코드의 실행시간을 측한다.

timeit.timeit()
timeit.timeit(stmt='pass',
              setup='pass',
              timer=<default timer>,
              number=1000000,
              globals=None)

    stmt: 실행측정할 코드 및 함수
    setup: stmt를 실행하기 위해 사전에 필요한 코드나 함수를 선언.
    setup의 실행 시간은 전체 측정 실행 시간에서 제외됨
    timer: Timer 인스턴스
    number: 선언한 stmt의 수행 횟수.
    선언하지 않으면 기본값으로 1000000번이 실행됨
    """

import random
import timeit


myl =[ random.randrange(1,1000) for w in range(100) ]
print( f"myl={ myl[0], myl[-1] }" )


t1 = timeit.timeit( 'a= 55 in [1,4,5,6,7,8,9,12,13,14,1,35, 9, 7, 6, 5, 34, 23]' )  # 줄 indent 규칙에 맞아야 함. 빈칸 없이 시작
print(f"time for x in List[] = {t1:12.7}" )

t1 = timeit.timeit( 'a= 55 in (1,4,5,6,7,8,9,12,13,14,1,35, 9, 7, 6, 5, 34, 23)' )  # 줄 indent 규칙에 맞아야 함. 빈칸 없이 시작
print(f"time for x in Tuple() = {t1:12.7}" )

