
# 윈도우에서는 첫번째로 호출된 후 얼마나 지났는지를
# wall-clock 초 단위 부동소수점으로 return합니다.
# return되는 값은 Wind32의 QueryPerformanceCounter()을 기준으로 합니다.

import time


N = 5000
print(" Time for ",  N, "\n Loops=", N*N )

start = time.time()
print(" start = ", start )
s = 0
for x in range( N ) :
    for y in range( N ) :
        s += 1


end = time.time( )
print(" end = ", end )
print(" 전체 시간(mili second)= ", end-start)
