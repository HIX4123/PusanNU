#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-16
#-------------------------------------------------------------------------------
"""
ncalls:    호출 수.
tottime:    주어진 함수에서 소비된 총 시간 (서브 함수 호출에 든 시간은 제외합니다)
percall:    tottime을 ncalls로 나눈 몫
cumtime:    이 함수와 모든 서브 함수에서 소요된 누적 시간 (호출에서 종료까지). 이 수치는 재귀 함수에서도 정확합니다.
percall:    cumtime을 프리미티브 호출로 나눈 몫
filename:lineno(function):     각 함수의 해당 데이터를 제공합니다 – 파일명:줄 번호(함수)

"""

import cProfile

def long_loop(N):
    for w in range(N):
        a = w
        a = a*a + a + w ;

    print(f' ending with {N}')


cProfile.run('long_loop(100)', 'mylog.txt') # 파일에 저장한다.
