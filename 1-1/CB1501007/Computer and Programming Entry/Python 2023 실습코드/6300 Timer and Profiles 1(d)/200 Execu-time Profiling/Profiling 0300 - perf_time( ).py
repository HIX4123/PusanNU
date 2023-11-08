#-*- coding: cp949 -*-


# 공식적으로 파이썬 3.3부터는 time.clock()대신 time.process_time() 이나
# time.perf_counter()을 쓸 것을 권장하고 있습니다.


import time

start = time.perf_counter()

N = 1000000

for i in range( N ) :
    a = 109813.0*1023801.2*i

delta = time.perf_counter() - start     # end에 코드가 구동된 시간 저장
print(" 1. Ellasped =", delta, " milli." )

for i in range( N ) :
    a = 109813.0*1023801.2*i
    b = a*a*a

delta = time.perf_counter() - start     # end에 코드가 구동된 시간 저장
print(" 2. Ellasped =", delta, " milli." )



