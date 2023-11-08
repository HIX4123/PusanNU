#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-03-28
#-------------------------------------------------------------------------------
from functools import cmp_to_key

P = [   (3,14),  (45, 9), (45, 4), (7,  9), \
      (51, 12), (-32, 19), (72,19), (33, 21), (45,21) ]

def mycmp( x ) :    #두번째 원소, 나이가 비교 기준
   return -x[1],x[0]

print("\n 실험1. P[]=", P)

Z = sorted(P )
print("\n 실험2. Z[]=")
for w in Z : print(w)

Q = sorted(P, reverse=True)
print("\n 실험3. 역순 Q[]=")
for w in Q : print(w)


print("\n 실험4. P[]=")
for w in P : print(w)

M = sorted( P, key= mycmp )
print("\n 실험5. M[]=")
for w in M : print(w)