
from itertools import combinations_with_replacement
n, k = 'iced jam plain'.split(), 2

print(list(combinations_with_replacement(n,k)))

print(len(list(combinations_with_replacement(list(range(10)), 3))))
