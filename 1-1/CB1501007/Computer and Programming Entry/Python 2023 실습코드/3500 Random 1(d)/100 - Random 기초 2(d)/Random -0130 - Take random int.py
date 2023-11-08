
# randint()와 randrange()의 차이

import random
N= 10

def dice( ):
    val = random.randint(1,6)
    return(val)

for x in range( N ) :
    print(" 주사위 call :", dice() )


print("\n Randrange() 활용하기 \n")

for x in range( N ) :
    fa = random.randrange(10,21,2 )
    print("10과 20 사이의 무작위 짝수 = ", fa)
