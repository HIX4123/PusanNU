
from itertools import cycle

mlist  = list("월화수목금토일")

pool = cycle( mlist)

i = 1
for item in pool :
    print("\n ", i, "=", item, end=' ')
    i +=1
    if i > 50 : break