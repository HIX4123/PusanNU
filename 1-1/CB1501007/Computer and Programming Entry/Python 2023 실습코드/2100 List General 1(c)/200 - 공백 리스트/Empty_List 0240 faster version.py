#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

foo= 0
row= 7 ; col = 10
tlist = [x[:] for x in [[foo] * col] * row ]    # for immutable

tlist[1][1]= 100

print("\n tlist= [ ")
for w in tlist :
    print(w)

print(" ] ")


