#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-21
#-------------------------------------------------------------------------------

# 야구에서 100게임, 4타석

import random

def hit_out( ) :
    cutval = random.random( ) # 0-1
    if cutval <= 0.3 :
        return("h")
    else :
        return ("o")


baseball=""
N=100*4
for w in range(N):
    baseball += hit_out( )

print(baseball)

olist= baseball.split("h")
for (i,w) in enumerate(olist):
    print(f'i={i:4}, {w}')

olist= baseball.split("o")
for (i,w) in enumerate(olist):
    print(f'i={i:4}, {w}')
