#-------------------------------------------------------------------------------

import sys
w = 1
print( len([w]), sys.getsizeof(w) )

L = [ ['a', 'b', 'c'], [345, ["Good",  "Kol"]], [(45 < 67)] ]


print("\n -------------- \n")
for w in L :
    print( "w=", w, "len(w)=", len(w), sys.getsizeof(w) )

print("\n -------------- \n")
T = list("Computer")
a = []
for w in T:
    print( len(a), sys.getsizeof(a) )
    a.append(w)

