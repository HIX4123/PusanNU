#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-04
#-------------------------------------------------------------------------------


import random

random.seed(456)

for i,w in enumerate(range(1,50,6)) :
    rnum = random.random()*1000 # 0과 1 사이의 random
    print(f'{w},  rnum= {rnum}')

random.seed(456)
print("\n 멋진 방법\n")

for i,w in enumerate(range(1,50,6)) :
    rnum = random.random()*1000 # 0과 1 사이의 random
    print(f'{w:3},  rnum= {rnum:7.3f}')
