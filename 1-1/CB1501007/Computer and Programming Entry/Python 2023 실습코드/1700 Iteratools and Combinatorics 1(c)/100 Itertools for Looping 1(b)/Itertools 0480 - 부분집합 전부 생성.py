import itertools


def powerset( X ) :
    i=0
    for L in range(0, len( X )+1):
        for subset in itertools.combinations( X, L):
            print(i, ":", subset)
            i += 1


stuff = [1, 2, 3, 4]
powerset( stuff )

powerset( [ "w", "Q", "+", ] )