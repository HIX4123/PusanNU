#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


from operator import itemgetter

L=[ [0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
sorted(L, key=itemgetter(2))

print("L=", L)



TL=[ (0, 1, 'f'), (4, 2, 't'), (9, 4, 'afsd')]
sorted(TL, key=itemgetter(2))

print("TL=", TL)