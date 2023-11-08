#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-01-02
#-------------------------------------------------------------------------------

from itertools import combinations, combinations_with_replacement

# the second argument is mandatory and specifies the length of the output tuples.
print("\n 중복이 없는 2개씩의 조합")
comb = combinations([1, 2, 3, 4], 2)
print(list(comb))

print("\n 중복이 없는 3개씩의 조합")
comb = combinations([1, 2, 3, 4], 3)
print(list(comb))

print("\n 중복을 허용하는 조합")
comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb))