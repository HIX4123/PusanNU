#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-06-05
#-------------------------------------------------------------------------------

"""

파이썬 3.7에서는 문제 없이 잘 쓰던 기능이 3.8에서는 사용할 수 없다.
time.perf_counter() 또는 time.process_time() 함수를 써야 한다.
"""

import time

ml= list() #[]             # profiling

print(0, "시작")
N=200000

point1 = time.process_time()
for w in range(N):
    ml.append(N-w-1)    # 뒤로 집어 넣기  N개 N초

print("1")

point2 = time.process_time()

ml=[]
for w in range(N):
    ml.insert(0,w)   # 리스트의 처음부터 집어넣기  N^2/2

print(2)
point3 = time.process_time()

print( f'append 시간= {point2-point1}')
print( f'insert 시간= {point3-point2}')