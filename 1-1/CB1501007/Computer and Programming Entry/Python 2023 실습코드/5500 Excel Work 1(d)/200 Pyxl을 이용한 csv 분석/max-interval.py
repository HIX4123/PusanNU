#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-04-02
#-------------------------------------------------------------------------------

# 리스트 L에서 어떤 구간의 합이 최대인 구간을 구하시오.
# 그 시작과 끝을 찻으시오

import random

random.seed(2019)

N = 12
L=[]

for w in range(N):
    su = random.randrange(-20,20)
    L.append( su )


print("L=", L )

for i in range(N) :
    for j in range(i,N) :
        print("i,j=",i,j, "L=",L[i:j+1], "sum=", sum(L[i:j+1]))
        # hint: sum( L )
