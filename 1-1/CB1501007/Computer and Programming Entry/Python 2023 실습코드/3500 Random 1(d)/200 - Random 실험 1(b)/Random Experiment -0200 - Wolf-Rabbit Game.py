
import random


world = 20*["R"]+ 6*["W"]  # 세상에는 20마리의 토끼와 6마리의 늑대가 있다.
print("현재상태 = ", world)


for x in range(10):
    a = world.pop(random.randrange(len(world)))
    b = world.pop(random.randrange(len(world)))
    print("=>", a, b, "\n", world)




# 두 마리가 우연히 이 공간에서 만난다.
#  a     b               결과
# (R, R) --> (R, R, R)        토끼 2마리는 새끼를 낳아 모두 3마리가 된다.
# (R, W) --> ( W )            늑대가 토끼를 잡아 먹는다.
# (W, W) --> (W) 또는 ( )     늑대 2마리가 만나면 싸워 둘 모두 죽거나 40%,
#                             한 마리만 죽는다. 50%
#                             그리고 10%의 경우 둘을 짝이 이뤄 새끼를 낳아
#                             모두 3마리가 된다.


# 만일 초기 상태에 토끼 20마리, 늑대 6마리가 있으면 생태계는 어떻게 될까 ?

world = 5*["R"]+ 3*["W"]
for steps in range( 10 ) :
    a = world.pop(random.randrange(len(world)))
    b = world.pop(random.randrange(len(world)))
    print("우연히 만난 동물은 =", a, b, end=' ')
    # 여러분은 이 부분을 채워 넣어야 합니다.
    world.extend([a,b])
    print(world)