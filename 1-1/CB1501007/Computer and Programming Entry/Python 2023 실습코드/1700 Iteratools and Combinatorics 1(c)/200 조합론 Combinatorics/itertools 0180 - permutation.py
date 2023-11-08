# https://docs.python.org/3/library/itertools.html#itertools.combinations

import itertools

L=[1,2,3,4,5]

print("\n itertools.permutations(L,3)")
for x in itertools.permutations( L, 3):
    print(x)


L=list("Beers")

print("\n itertools.permutations(Beers,5)")
for x in itertools.permutations( L, 5):
    print(x)


def Nperm(L):
    yield( itertools.permutations( L, len(L) ) )


L=list("Booky")
for w in range(40):
    print( Nperm(L))


