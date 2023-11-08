
from itertools import cycle

mlist  = list("computer")

pool = cycle( mlist)

i = 1
for item in pool :
    print(i, "=", item, end=' ')
    i +=1
    if i > 50 : break