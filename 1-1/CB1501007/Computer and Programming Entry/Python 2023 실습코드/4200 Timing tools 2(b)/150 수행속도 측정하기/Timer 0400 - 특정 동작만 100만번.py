#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-05-03
#-------------------------------------------------------------------------------

#
# https://brownbears.tistory.com/456
# 기본이 100만번 해당 함수를 수행한 시간을 계산해준다.

import timeit


t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"t1={t1}")






t2 = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
print(f"t2={t2}")

def test():
    return "-".join(str(n) for n in range(100))

t3 = timeit.timeit('test()', setup='from __main__ import test', number=10000)
print(f"t3={t3}")

