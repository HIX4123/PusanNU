
import random


print("[a,b] 사이의 random real number 만들기")

def real_random(a,b):
    t = random.random()
    w = (1-t)*a + t*b
    return w

for x in range(10):
    print(x, "=", real_random(1.345,1.792))



for x in range(10):
    print(x, "=", real_random( -11.5, +8.023))