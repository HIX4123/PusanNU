

def parray( Q ):
    for i,x  in enumerate(Q) :
        print(i, "= ",  x, "\n")



n = 3
m = 4
a = [ [] ]
for i in range(n):
    a.append([[]] * m)


parray( a )



