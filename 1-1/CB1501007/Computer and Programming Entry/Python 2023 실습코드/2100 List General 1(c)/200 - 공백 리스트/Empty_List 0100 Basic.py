#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

foo= 0
tlist = []
row= 7 ; col = 10
for i in range (0, row):
    new = []
    for j in range (0, col):
        new.append(foo)
    tlist.append(new)

print("\n tlist= [ ")
for w in tlist :
    print(w)

print(" ] ")