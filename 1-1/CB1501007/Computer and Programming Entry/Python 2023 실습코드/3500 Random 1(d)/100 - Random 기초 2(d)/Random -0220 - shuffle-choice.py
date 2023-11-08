
import random

abc = ['a', 'b', 'c', 'd', 'e', 'w', 'z', '+', '@']
random.shuffle(abc)
print(abc)
random.shuffle(abc)
print(abc)
random.shuffle(abc)
print(abc)

new = random.sample(abc,5)
print("sampling 이후에 원본은 변하지 않음")
print(abc)
print(new)


print("choice() 하나를 선택함. 원본은 변화없음")


menu = ['쫄면', '육계장', '비빔밥' ]
print(random.choice(menu))
print(random.choice(menu))
print(random.choice(menu))
print(random.choice(menu))


