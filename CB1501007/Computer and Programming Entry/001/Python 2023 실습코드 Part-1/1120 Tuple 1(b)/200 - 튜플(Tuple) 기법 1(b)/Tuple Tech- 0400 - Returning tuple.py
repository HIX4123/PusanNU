

def maxmin(a,b) :
    if a > b : return (a,b)
    else : return (b,a)

def printall(*args):  # 가변길이의 tuple
    sum = 0
    newt= []
    for x in args :
        print(x)
        sum += x
        newt.append( sum )

    return tuple(newt)



t = divmod(7, 3)
print("divmod = ", t)

t = maxmin( 12, 55 )
print(t)
t = maxmin( 88, 55 )
print(t)


t = printall( 3, 4, 5, 10 )
print(t)


t = printall( 1, 2, 3, 4, 5, 10 )
print(t)


