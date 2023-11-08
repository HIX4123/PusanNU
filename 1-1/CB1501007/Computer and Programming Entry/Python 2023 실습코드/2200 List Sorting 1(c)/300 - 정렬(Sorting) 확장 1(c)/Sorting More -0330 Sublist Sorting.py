
tlist=[ [3,5,6], [0,9,4], [9,1,2], [0,2,8], [8,1,4], [5, 3, 2], [1, 8,3], [9,1,4] ]

alist = sorted( tlist )

print("\nalist= ")
for w in alist :
    print(w)


blist = sorted( tlist,  reverse=True )
print("\nblist= ")
for w in blist :
    print(w)


clist = sorted( tlist, key=lambda x: x[2] ) #, reverse=True )


print("\nclist= ")
for w in clist :
    print(w)