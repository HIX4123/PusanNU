#-*- coding: cp949 -*-


import time

start = time.time()
N = 1000000

for i in range( N ) :
    a = 109813.0*1023801.2*i


delta = time.time() - start     # end에 코드가 구동된 시간 저장

print("Ellasped =", delta, " milli seconds" )



