#--------------------------------------------------------
# Author:      Zoh Que
# Created:     30-01-2023
#--------------------------------------------------------

import itertools

chars = ['A', 'B', 'C']

p = itertools.permutations(chars, 3)  # 순열
c = itertools.combinations(chars, 2)  # 조합

print(list(p))
print(list(c))