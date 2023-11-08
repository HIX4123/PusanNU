
import time

# 좀 나쁜 방법, 권장하지 않음

N = 5000
print(" Time for ",  N, "\n Loops=", N*N )

start = time.time()
print(f" start = {start:.5f}" )
s = 0
for x in range( N ) :
    for y in range( N ) :
        s += 1


end = time.time( )
print(f" end = = {end:.5f}" )
print(f" 전체 시간(mili second)= {end-start:8.5f}")
