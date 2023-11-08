#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-04
#-------------------------------------------------------------------------------

## ncalls  : 함수의 호출 횟수
## tottime : 함수에서 소비 된 총 시간
## percall : 함수의 호출에 사용된 시간을 호출 횟수로 나눈 값
##           tottime을 ncalls로 나눈 값
## cumtime : 다른 함수 호출을 포함하여 함수에서 보낸 시간
## filename:
## lineno  : 파일명과 해당하는 행 번호

import cProfile

def Func1():
    for i in range(100000):
        t = i * i


def Func2():
    for i in range(100000):
        t = (i/2) * (i/3) * (i/5)


cProfile.run('Func1()')
cProfile.run('Func2()')