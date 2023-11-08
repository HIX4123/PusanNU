
from random import choice, sample

sa = set(range(1,21))
print(sa)

for w in range(10):
    q = sample( sa, 4)
    print(q)