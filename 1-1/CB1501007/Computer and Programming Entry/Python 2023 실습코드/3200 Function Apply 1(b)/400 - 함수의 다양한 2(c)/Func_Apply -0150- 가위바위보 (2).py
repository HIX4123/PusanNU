#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-21
#-------------------------------------------------------------------------------


import random


def son( ):
    gbb=["가위", "바위", "보"]
    result = random.choice( gbb )
    return( result )


def seven_son( K ) :
    S=[]
    for w in range(K ):
        S.append( son() )

    return( S )


N= 100000
count = 0
for w in range( N ):
    Q = seven_son( 22 )
    if Q.count("가위")>=1 and Q.count("가위")>=1 and Q.count("가위")>=1 :
        #print( Q, "  무효")
        count += 1


print(N, count, count/N )






