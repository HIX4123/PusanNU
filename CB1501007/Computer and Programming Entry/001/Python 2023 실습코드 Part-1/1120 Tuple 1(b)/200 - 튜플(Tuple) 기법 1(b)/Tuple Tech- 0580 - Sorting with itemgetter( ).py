#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

from operator import itemgetter

TL=[ (0, 1, 'foo'), (9, 1, "몽"), (4, 2, 'table'), \
     (9, 4, 'sonoma'), (6,0,"똥"), (4, 7, "Busan")]

T1 = sorted( TL )
for w in T1 :
    print(w)

print(f"\n itemgetter(1) 사용후 ")
T1 = sorted(TL, key=itemgetter(1))
for w in T1 :
    print(w)


print(f"\n itemgetter(2) 사용후 ")
T1 = sorted(TL, key=itemgetter(2))
for w in T1 :
    print(w)


