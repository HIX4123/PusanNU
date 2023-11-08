#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-15
#-------------------------------------------------------------------------------


L = list("부산산성막걸리")
print(f'처음 {L}')

T = L
S = L[:]
W = list(L)

L.append("통")
print(f' append 후 L[] = {L}')
print(f' append 후 T[] = {T}')
print(f' append 후 S[]:= L[:] = {S}')
print(f' append 후 W[]= {W}')