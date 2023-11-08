"""
파이썬 3.3+ 이상부터 perf_counter와 process_time를 사용할 수 있는데  차이점은 다음과 같습니다.
perf_counter는 sleep 함수를 호출하여 대기한  시간을 포함하여 측정합니다.
process_time는 실제로 연산하는데 걸린 시간만 측정합니다.
"""

import time


# https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py
def calcPi(limit):  # Generator function
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr

def looping(N):
    for i in range( N ) :  # 시간을 측정하고자 하는 code
        a = 109813.0*1023801.2*i
    return()

N= 100000000
start = time.perf_counter()
looping(N)
end = time.perf_counter()
print(f'> Looping perf_counter: {end-start:.4e} seconds')

start = time.process_time()
looping(N)
end = time.process_time()
print(f'> Looping process_time: {end-start:.4e} seconds')

start = time.perf_counter()
calcPi(N)
end = time.perf_counter()
print(f'> 파이 계산 perf_counter: {end-start:.4e} seconds')

start = time.process_time()
calcPi(N)
end = time.process_time()
print(f'> 파이 계산 process_time: {end-start:.4e} seconds')