
tlist=[ (3,5,6), (0,9,4), (10,1,2), (0,2,8), (8,1,4), (5, 3, 2), (1, 8,3), (10,1,4)]

alist = sorted( tlist )

blist = sorted( tlist, key=lambda x: x[2], reverse=True )
print(alist)
print(blist)