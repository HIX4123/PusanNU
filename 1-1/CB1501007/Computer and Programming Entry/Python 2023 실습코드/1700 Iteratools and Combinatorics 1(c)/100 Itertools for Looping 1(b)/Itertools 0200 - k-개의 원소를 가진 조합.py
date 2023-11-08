#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-30
#-------------------------------------------------------------------------------


import itertools
import string

my_list = [1,2,3,4]

print("\n 2개씩의 모든 가능한 Pair ")
for pair in itertools.product(my_list, repeat=3):
    print(*pair)

print("\n 2개씩의 조합 ")
for (i,pair) in enumerate(itertools.combinations(my_list,2)):
    print( f"{i:3}: ({pair[0]},{pair[1]})")

print("\n 3개씩의 조합 ")
slist=list(string.ascii_lowercase)[:7]
for (i,pair) in enumerate(itertools.combinations( slist,3)):
    print( f"{i:3}: ({pair[0]},{pair[1]},{pair[2]})")

for (i,pair) in enumerate(itertools.permutations( slist,3)):
    print( f"{i:3}: ({pair[0]},{pair[1]},{pair[2]})")