#--------------------------------------------------------
# Author:      Zoh Que
# Created:     31-01-2023
#--------------------------------------------------------
import timeit
import random

def random_gen(N):
    for x in range(N):
        random.random()

for w in range(5):
    time1 = timeit.timeit(stmt='random_gen(100)', \
            setup='from __main__ import random_gen', number=w)
    print(f"w={w}, time={time1:.3e}")