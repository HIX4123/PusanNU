# https://docs.python.org/3/library/itertools.html#itertools.combinations

import itertools

L=[1,2,3,4,5]


print("\n itertools.permutations(L,2)")
for x in itertools.permutations( L, 2):
    print(x, end=' ')



print("\n itertools.permutations(L,3)")
for x in itertools.permutations( L, 3):
    print(x, end=' ')

