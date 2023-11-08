#--------------------------------------------------------
# Author:      Zoh Que
# Created:     30-01-2023
#--------------------------------------------------------

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]

for p in permute( list("Books")):
    print( p)


print( ">> ------------- << \n\n")
mygen = permute( list("IPA_box"))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print( ">> ------------- << \n\n")
mygen = permute( list("box_IPA"))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
