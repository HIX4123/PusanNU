
from itertools import cycle

mlist  = list("computer")

pool = cycle( mlist)

print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))
print(next(pool))


i=1
index = 1
while True:
    print(i, "= ",  mlist[index])
    index = (index + 1) % len( mlist)
    i += 1
    if i > 30 : break