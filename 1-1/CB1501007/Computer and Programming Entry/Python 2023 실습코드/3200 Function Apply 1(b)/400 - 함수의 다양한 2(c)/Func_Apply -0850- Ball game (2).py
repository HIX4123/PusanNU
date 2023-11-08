#-------------------------------------------------------------------------------
# A Game.  You throw a ball to the 10 empty boxes.
# The ball will occupy a box randomly.
# The game stop if a ball occupies a box not empty.
# Compute the average number of throwing.
# Assume that you shoul pay 5000 KW for this game.
# Then you get 1000 KW for each throwing action.
# Do you accent this game ? Or not

import random   # for random
random.seed( )  # 씨앗(seed)값 설정하기. 시간 정보에 의해 초기화됨



def throw_ball( thisbox ):
    putbox = random.choice( list(range(10)))
    thisbox[putbox] += 1
    if thisbox[putbox] >= 2 : return("Over")
    else :
        return("Go")

box=[0,0,0,0,0,0,0,0,0,0]

for x in range(20) :
    result = throw_ball( box )
    print(result, box)
    if result == "Over" : break



