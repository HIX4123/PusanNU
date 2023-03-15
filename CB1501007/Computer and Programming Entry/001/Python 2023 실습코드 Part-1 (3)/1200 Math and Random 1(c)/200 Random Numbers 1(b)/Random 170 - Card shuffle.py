#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------

import random

def makecard():
    deck=[]
    for t in list("SHDC") : # SPADE Heart Diamond Clover
        for w in list("a23456789tJQK") :
            myc = t+"-"+w
            deck.append(myc)

    #print(deck)
    return( deck)





casino = makecard()
random.shuffle( casino ) # 카드를 섞음


print( "first   player=", casino[:7] )
print( "second  player=", casino[7:14] )