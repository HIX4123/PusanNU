#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-04-04
#-------------------------------------------------------------------------------

# >> python this.py a b c d e

# 만일 pyscripter에서 사용할 경우에는 Run의 option으로 넣을 수 있다.
#
# > Run > Command Line Parameters를 enable 시킬 수 있다.1

import sys
import os

myb = int(sys.argv[1] )
mye = int(sys.argv[2] )

S = 0
for w in range(myb, mye+1):
        S += w

print(f"{myb}부터 {mye}까지 합은 {S}")