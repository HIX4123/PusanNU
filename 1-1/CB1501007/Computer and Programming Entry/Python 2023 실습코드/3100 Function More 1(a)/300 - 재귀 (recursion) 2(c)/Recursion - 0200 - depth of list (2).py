
def depth( L ):
    if isinstance( L , list):
        return 1 + max( depth(item) for item in L )
    else:
        return 0



mlist = [ 2, 3, 4, [ 7, 8, [ 9, 0 ], 5 ] , 2 ,3 ]

Ulist= [ 45, 67, [[[34]]], [4, 5, [6]], [[[[9],67]]]]

print("depth = ", depth( mlist ))

for w in Ulist :
    print( f'w={w},  its 깊이는 ={ depth(w)}' )
