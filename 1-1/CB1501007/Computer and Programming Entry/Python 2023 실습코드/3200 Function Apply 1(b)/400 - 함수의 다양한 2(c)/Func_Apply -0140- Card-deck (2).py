
import random
random.seed( 41234 )        # Random Number 시작점을 설정

def mydice( ) :
    mark=[1,2,3,4,5,6]
    return ( random.choice(mark) )


def makecard( ) :
    deck= [ ]
    shape=["d", "s", "c", "h"]
    num=["1","2","3","4","5","6","7","8","9","10","J", "Q", "K"]
    for x in shape :
        for y in num :
            deck.append(x+"-"+y)
    return(deck)



newdeck = makecard()
print("\n 초기=", newdeck)

random.shuffle( newdeck )
print("\n 섞은 후=", newdeck)