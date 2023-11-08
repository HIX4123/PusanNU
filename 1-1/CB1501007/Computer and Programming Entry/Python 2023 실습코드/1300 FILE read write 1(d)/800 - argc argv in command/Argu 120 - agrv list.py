
# 사용법
# > python this.py arg1 arg2 arg3

import sys
import os


if len(sys.argv) == 0:
    print(" Usage: > python arg0 arg1 arg2....  하나 이상 사용해야 함")
    sys.exit()

for i,w in enumerate(sys.argv) :
    print(f' arg{i} = {w}')
