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

myfile= os.path.basename(__file__)
print("myfile=", myfile)
print(f"sys.argv list[] = {sys.argv[1:]}")

L= sys.argv[0].split('\\')
print("file name= ", L[-1])
for i, arg in enumerate(sys.argv[1:]):
    print(f"Argument {i:>6}: {arg}")
