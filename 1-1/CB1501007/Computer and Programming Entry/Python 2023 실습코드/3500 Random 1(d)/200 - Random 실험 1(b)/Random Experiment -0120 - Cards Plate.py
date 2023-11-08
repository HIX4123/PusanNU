
import random   # for random
random.seed()   # 씨앗(seed)값 설정하기. 시간 정보에 의해 초기화됨

sym = ['S', 'D', 'H', 'C']
num = [ 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]

deck = []

for x in sym : # 카드 만들기
    for y in num :
        tcard = x+'-'+y
        deck.append( tcard )


print(deck)
random.shuffle( deck )
print(deck)


