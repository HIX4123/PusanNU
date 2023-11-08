#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

myl = [ [1,2,3,4,5], [11,21,31,41,51], [10, 9, 8, 7, 6, 5, 4], [-1,-2,-3,-4] ]

print("1. Out= ", myl[1:3])
print("2. Out= ", myl[1][2:-1])
print("3. Out= ", myl[3][:-2])
print("4. Out= ", myl[0][2:])
print("5. Out= ", myl[-1][:3])


print("\n imlist= ")
imlist= range(10,40,3)
for w in imlist :
    print (w)

print("\n ylist= ")
ylist = imlist[5:20]
for w in ylist :
    print (w)


