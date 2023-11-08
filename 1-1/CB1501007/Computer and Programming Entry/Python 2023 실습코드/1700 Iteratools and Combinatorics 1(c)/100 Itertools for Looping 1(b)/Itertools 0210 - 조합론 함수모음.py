# https://docs.python.org/3/library/itertools.html#itertools.combinations

import itertools

L=[1,2,3,4,5]

for x in itertools.combinations(L, 2) :
    print(x)

sum = 0
print("\n itertools.count")
for x in itertools.count( 10 ):
    print(x, end=' ')
    sum += x
    if sum > 200 : break

sum = 0
print("\n itertools.cycle")
for x in itertools.cycle( "ComputerBox" ):
    print(x, end=' ')
    sum += 1
    if sum > 20 : break

print("\n itertools.product()")
for x in itertools.product('ABCD', repeat=2):
    print(x, end=' ')

print("\n itertools.permutations()")
for x in itertools.permutations('ABCD', 2):
    print(x, end=' ')

print("\n itertools.combinations()")
for x in itertools.combinations('ABCDEFG', 3):
    print(x, end=' ')

print("\n itertools.combinations_with_replacement()")
for x in itertools.combinations_with_replacement('ABCDEFG', 3):
    print(x, end=' ')

