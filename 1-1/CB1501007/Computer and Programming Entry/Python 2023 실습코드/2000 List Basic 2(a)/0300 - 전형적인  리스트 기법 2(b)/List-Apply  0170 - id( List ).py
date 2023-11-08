#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-15
#-------------------------------------------------------------------------------

import copy


a = ["10", "20"]
b = a[:]
c = a
d = c
e = copy.deepcopy(a)

print(f' a[]={a}, id(a)= {id(a)}' )
print(f' b[]={b}, id(b)= {id(b)}' )
print(f' c[]={c}, id(c)= {id(c)}' )
print(f' d[]={d}, id(d)= {id(d)}' )
print(f' e[]={e}, id(e)= {id(e)}' )