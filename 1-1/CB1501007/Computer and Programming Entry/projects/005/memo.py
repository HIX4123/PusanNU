import random as rand

step = [+1, 0, -1]
pok = 2

average = 0

for j in range(100000):
    H = 0
    i = 1
    while True:
        H += rand.choice(step)
        if H > pok or H < -pok:
            break
        i += 1
    average += i

print(average / 100000)