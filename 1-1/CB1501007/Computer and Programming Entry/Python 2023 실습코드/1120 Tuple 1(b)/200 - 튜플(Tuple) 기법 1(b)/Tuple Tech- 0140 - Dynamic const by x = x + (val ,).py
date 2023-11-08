import random

N=30
myt=()
for w in range(N) :
    val = random.randrange(10)
    myt = myt + (val,)


print(myt)
