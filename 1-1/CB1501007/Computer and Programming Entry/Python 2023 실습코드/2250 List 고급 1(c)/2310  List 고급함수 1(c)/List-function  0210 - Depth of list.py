
def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0



mlist = [ 2, 3, 4, [ 7, 8, [ 9, 0 ], 5 ] , 2 ,3 ]


print("depth = ", depth( mlist ))
