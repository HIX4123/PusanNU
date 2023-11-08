
from operator import itemgetter

ml = [ [1,1], [1,2], [1,3], [2,1], [2,2], [2,4],
       [3,1], [3,3], [3,4], [4,1], [4,2], [4,3] ]


print( "\n Test 1. 일반 ", sorted(ml              ) )
print( "\n Test 2. 역순", sorted(ml, reverse=True) )
print( "\n Test 3. 두번째 ", sorted(ml, key=itemgetter(1)))
print( "\n Test 4. 두번째 역순", sorted(ml, key=itemgetter(1), reverse=True))
