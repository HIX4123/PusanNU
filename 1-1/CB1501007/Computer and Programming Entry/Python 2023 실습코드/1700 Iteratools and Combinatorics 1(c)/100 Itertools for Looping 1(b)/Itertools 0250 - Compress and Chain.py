# https://docs.python.org/3/library/itertools.html#itertools.combinations

import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

print(itertools.chain(letters, booleans, decimals))


print("Out 1=", list( itertools.chain(letters, booleans, decimals) ))

print("Out 2=", list([x for x in numbers if x % 2]))

print("Out 3=", list(itertools.compress(letters, booleans)))

print(list(map(None, numbers, decimals)))

