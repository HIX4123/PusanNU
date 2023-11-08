
from operator import itemgetter

ml = [ [1,1], [1,2], [1,3], [2,1], [2,2], [2,4],
       [3,1], [3,3], [3,4], [4,1], [4,2], [4,3] ]


print( "\n Test 1. 일반 ", sorted(ml              ) )
print( "\n Test 2. 역순", sorted(ml, reverse=True) )
print( "\n Test 3. 두번째 ", sorted(ml, key=itemgetter(1)))
print( "\n Test 4. 두번째 역순", sorted(ml, key=itemgetter(1), reverse=True))



print( "\n Test 5. 첫번째 Increase ", sorted(ml) )

#새로운 비교함수를 Lambda로 만듬.
mykey=lambda x: (x[0], x[1]*-1)
print( "\n Test 6. 5번에서 두번째 key 역순", sorted(ml, key=mykey) )

#key=lambda x: (x[0], x[1]*-1)

