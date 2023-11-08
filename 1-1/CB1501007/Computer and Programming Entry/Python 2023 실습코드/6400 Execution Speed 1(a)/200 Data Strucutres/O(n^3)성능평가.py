#-------------------------------------------------------------------------------
# Author:      Zoh, 알고리즘 Order를 보여주기 위하여 만들어 봅니데이.
# Created:     2021-03-05
#-------------------------------------------------------------------------------

"""
time.clock( )는 더 이상 사용되지 않음. 헐... 대신에
time.perf_counter() 또는 time.process_time() 함수를 써야 한다.
"""

import time

Ln= [100, 200, 300, 400, 500, 600] # 64만까지 하면 디짐.


print("\n O(n*n*n) 알고리즘의 성능")

for N in Ln :
    ml = []
    tbegin= time.process_time()

    for w1 in range(N) :
        for w2 in range(w1) : # 시작!
            for w3 in range(w2) :
                ml.append(w1+w2+w3)

    tend = time.process_time()              # 끝 땡!

    print( f'N={ N:7} elapsed= {tend-tbegin:7.4f} sec.')


