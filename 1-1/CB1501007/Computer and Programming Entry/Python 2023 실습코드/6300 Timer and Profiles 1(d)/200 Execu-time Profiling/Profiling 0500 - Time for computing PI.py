# 파이썬 3.3+ 이상부터 perf_counter와 process_time를 사용할 수 있는데
# 차이점은 다음과 같습니다.

# perf_counter는 sleep 함수를 호출하여 대기한  시간을 포함하여 측정합니다.
# process_time는 실제로 연산하는데 걸린 시간만 측정합니다.



import time

# https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py
def calcPi(limit):  # Generator function
    # Prints out the digits of PI   until it reaches the given limit

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    yield n # yield digit
                    if counter == 0: # insert period after first digit
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


start = time.perf_counter()
calcPi(1000)
end = time.perf_counter()
print('PI perf_counter:', end-start, 'seconds')

start = time.process_time()
calcPi(1000)
end = time.process_time()
print('PI process_time:', end-start, 'seconds')
