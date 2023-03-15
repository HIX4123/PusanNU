
import time


N = 5000
print(" Time for ",  N, "\n Loops=", N*N )

start = time.process_time() # time.clock( ) 더 이상 쓰이지 않음
print(" start = ", start )
s = 0
for x in range( N ) :
    for y in range( N ) :
        s += 1


end = time.process_time()
print(" end = ", end )
print(" 전체 시간(mili second)= ", end-start)
