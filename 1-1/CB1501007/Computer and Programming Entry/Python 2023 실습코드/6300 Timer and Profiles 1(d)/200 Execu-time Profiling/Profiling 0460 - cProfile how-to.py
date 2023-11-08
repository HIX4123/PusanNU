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

def Fibonacci_Recursion(val):
    if (val == 1):
        return 0
    elif (val == 2):
        return 1
    else:
        return Fibonacci_Recursion(val - 1) + Fibonacci_Recursion(val - 2)

def Fibonacci_Repeat(val):
    val_1 = 0
    val_2 = 1
    val_3 = 0
    temp  = 0

    if (val == 0):
        return 0
    elif (val == 1):
        return 1
    else:
        for i in range (0, val):
            temp = val_2
            val_2 = val_1 + val_2
            val_1 = temp

        return val_2

def TEST():
    recursion = 0
    repeat = 0

    recursion = Fibonacci_Recursion(30)
    repeat    = Fibonacci_Repeat(30)

    print(recursion, repeat)

if __name__ == "__main__":
    cProfile.run("TEST()")
    #TEST()
