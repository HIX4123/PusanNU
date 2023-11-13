import random


def recurse():
    # equally likely values 1, 2, 3
    x = random.choice([1, 2, 3])
    if x == 1:
        return 3
    elif x == 2:
        return 5 + recurse()
    else:
        return 7 + recurse()

for _ in range(10000):
    print(recurse())