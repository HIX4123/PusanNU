#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-05-02
#-------------------------------------------------------------------------------



L = [ 21, -32, 5, 6, -11, 24, 78, -10, 9, 20]


Nega=[ w*w   if w > 0 else w+100 for w in L ]
print("Experi 1= ", Nega)



Nega=[ 2*w  if w > 0 else 10*w for w in L ]
print("Exper2 1= ", Nega)


Nega=[ w  for w in L if w < 0  ]
print("Exper3 1= ", Nega)
Q=[]
for w in L:
    if w > 0 :
        Q.append(w*w)
    else :
        Q.append(w+100)






