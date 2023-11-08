#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-10-07
#-------------------------------------------------------------------------------

import itertools

pool = ['A', 'B', 'A', 'C']
alist = list(map(''.join, itertools.permutations(pool)))    # 3개의 원소로 수열 만들기
blist = list(map(''.join, itertools.permutations(pool, 2))) # 2개의 원소로 수열 만들기

print("\n alist= ", alist )
print("\n blist= ", blist )