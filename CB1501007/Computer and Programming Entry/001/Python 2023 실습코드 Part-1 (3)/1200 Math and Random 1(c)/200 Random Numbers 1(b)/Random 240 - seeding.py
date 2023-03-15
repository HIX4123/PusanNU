
# Random클래스의 경우 특별히 생성자를 호출하여 클래스 인스턴스를 생성하거나
# 클래스메서드를 호출하지는 않았다.
# 그 이유는 random.Random클래스의 인스턴스객체가 내부적으로 숨겨져 생성되었기 때문이다.
# 이러한 숨겨진 Random객체에 대해서는 seed값을 전달하지 않았기 때문에 시스템 시간
# 값을 사용한다. 만약 아래와 같이 명시적으로 두 Random객체를 생성하고 seed값을
# 동일하게 주면, 두 객체가 생성하는 임의 값은 동일하게 된다.
#
import random


random.seed(1) #seed값을 1로 주고 Random객체를 생성
N= 5
print("\n seed=1 \n")
for x in range(N):
    print(" Random=", random.randrange(100))

print("\n 또 다시 seed=1 \n")
random.seed(1) #seed값을 1로 주고 Random객체를 생성
N= 5
for x in range(N):
    print("New Random=", random.randrange(100))


print("\n Another Random")
for x in range(N):
    print("Random=", random.randrange(100))

R2 = random.Random() #seed값 없이 Random객체를 생성(시스템 시간 값이 사용됨)
print("\n Another Random R2")
for x in range(N):
    print("Random=", random.randrange(100))


R2.seed(1) #이미 생성된 Random객체의 seed값을 변경
print("\n Another Random R2 - seed changing")
for x in range(N):
    print("Random=", random.randrange(100))


