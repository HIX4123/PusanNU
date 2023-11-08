#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-16
#-------------------------------------------------------------------------------


# do-while은 C/C++에는 있지만 python에는 없습니다.
# 이것을 야매로 만들어 봅니다.
# while( )과 do-while( )의 차이는 TASK를 한번 반드시
# 수행하는가 아닌가에 있습니다.

"""
do {
   TASK ;
   } while ( condition )
"""

adden=0
mysum=0
Limit= 1000

while( True ) :
    adden += 1
    mysum = mysum + adden

    if mysum > Limit : break

    print( adden, mysum)

