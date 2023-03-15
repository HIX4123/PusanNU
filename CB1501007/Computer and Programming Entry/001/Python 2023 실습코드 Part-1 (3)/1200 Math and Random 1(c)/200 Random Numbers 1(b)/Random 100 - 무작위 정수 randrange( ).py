

import random


print("주사위 Simulation")

for x in range(20):
    print(x, "=", random.randrange(1,7))


card = ["비", "풍", "초", "똥", "광", "삼"]

for x in range(12):
    w = random.choice( card )
    print(w)