
import random


menu = [ "짜장", "짬뽕", "순대", "소주", "피자", "만두", "맹물", "빠나나"]


my = random.sample( menu, 3)
for x in my :
    print(x, "의 위치=",  menu.index(x))


print("\n 또 다른 선택")
my = random.sample( menu, 4)
print(my)