# Purpose: 무작위  함수를 사용한 주사위, 카드 놀이 만들기
#!/usr/bin/env python
#-------------------------------------------------------------------------------
import random
random.seed(1234)               # Random Number 시작점을 설정

for i in range(10) :
    print(i, random.random()) # 10개의 무작위수[0,1]를 생성한다.

# Fenerating random numbers between 1 to 100
print("\n 특정 범위내의 무작위수 만들기 예) 1에서 100사이")
for i in range(10) :
    print(i,"=", random.randrange(1,101))


mylist=["oh", "my", "boy", "summer", "time", "will", "come", 98, True ]


random.shuffle( mylist )
print("after shuffle=", mylist)

# We can select an item randomly from a list
for i in range(10) :
    print(i, random.choice( mylist )) # 10개의 무작위수[0,1]를 생성한다.