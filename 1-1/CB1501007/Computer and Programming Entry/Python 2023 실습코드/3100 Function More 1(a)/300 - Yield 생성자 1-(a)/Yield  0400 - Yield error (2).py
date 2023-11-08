
def gen():
    yield 'one'
    yield 'two'
    yield 'three'

g = gen()

print((next(g)))  # one
print((next(g)))  # two
print((next(g)))  # three
#print(next(g))  # raise StopIteration
#print(next(g))
