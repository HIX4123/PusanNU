
# 집합에서 임의의 한 원소를 선택하는 방법

my_set = set("HelloWorld")
print(my_set)

# pop a random element # 리스트의 경우 myl.choice( )
print((my_set.pop()))

# pop a random element
my_set.pop()
print(my_set)

# clear my_set, Output: set()
my_set.clear()
print(my_set)

#리스트의 경우라면
import random

la=[1,2,3,4,5]
x= random.choice(la)
#