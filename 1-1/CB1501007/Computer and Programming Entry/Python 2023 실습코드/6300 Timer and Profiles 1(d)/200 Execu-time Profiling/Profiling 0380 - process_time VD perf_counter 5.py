#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-04
#-------------------------------------------------------------------------------

# time.perf_counter, time.process_time인데 두가지는 차이점이 있다.
# time.process_time는 실제로 연산에 소요된 시간만 측정한다.
# sleep, file io등에 소요된 시간은 제외된다. )
# time.perf_counter는 전체적으로 흐른 시간을 측정한다.

from time import (
    process_time,
    perf_counter,
    sleep, )

mybegin= process_time()
print("0. 시작 시간=", mybegin )
sleep(3)
print("1. prcess time=", process_time() - mybegin )

mybegin= perf_counter()
print("2. perf_counter=", mybegin )
sleep(3)
print("3. perf time =",perf_counter()-mybegin)



