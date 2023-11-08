#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-05-02
#-------------------------------------------------------------------------------



L = [ 21, -32, 5, 6, -11, 24, 78, -10, 9, 20]


Nega=[ w  for w in L if w < 0 ]
print("Experi 1= ", Nega)


Nega=[ w+10  for w in L if w < 0 ]
print("Experi 2= ", Nega)

Nega=[ [w]  for w in L if w < 0 ]
print("Experi 3= ", Nega)



