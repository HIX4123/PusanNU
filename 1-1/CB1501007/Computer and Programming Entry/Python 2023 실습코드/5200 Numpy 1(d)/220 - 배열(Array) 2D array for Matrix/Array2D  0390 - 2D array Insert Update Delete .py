
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print((T[0]))
print((T[1][2]))

print("\n Initial T[]")
for r in T:
    for c in r:
       print(c, end=' ')
    print()


T.insert(2, [0,5,11,13,6])
print("\n After Insert")
for r in T:
    for c in r:
       print(c, end=' ')

    print()



T[2] = [11,9]
T[0][3] = 7
print("\n After Updating")
for r in T:
    for c in r:
       print(c, end=' ')

    print()


del T[3]
print("\n After Deleting")
for r in T:
    for c in r:
       print(c, end=' ')

    print()

