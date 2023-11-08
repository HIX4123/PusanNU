# time.clock( )은 더이상 지원되지 않습니다. 2021년 3월 봄날에


import time

N = 100000

def looping(N):
    for i in range( N ) :  # 시간을 측정하고자 하는 code
        a = 109813.0*1023801.2*i
    return()


for w in range(1,5):
    mstart = time.process_time()
    looping(N)
    mend   = time.process_time()
    delta =  mend - mstart     #
    print(f"N={N:.4e}, Ellasped = {delta:.3e}  seconds." )
    N *= 10






