
def maxlast( L ) :
    n = len(L)
    #print "Current Stack", L, "L=", n
    for i in range(n-1) :
        if L[i] > L[i+1] :
           return(i)

    return(i+1)

def Lswap( L, t ):
    #print "Lswap(1) = ", L, "t=", t
    mx = 10000
    for i in range(t):
        if L[i] > L[t] :
            diff = L[i] - L[t]
            #print "diff=", diff
            if mx > diff :
                mx = diff
                this = i

    temp=L[t]
    L[t]=L[ this ]
    L[this]=temp
    L[0:t]= sorted(L[0:t],reverse=True)
    #print "Lswap(2) = ", L


# 시작은 top [7, 6, 5, 4, 3, 2, 1]
# 끝은       [1, 2, 3, 4, 5, 6, 7 ]

n = 7
S = [ 6, 5, 4, 3, 2, 1 ]

i = 1
while( i < 1000 ):
    print("Current Stack[ %4d ]= " % (i), S)
    e = maxlast( S )
    if e+1 == len(S) :
        print("\nEnd of permute")
        break

    Lswap(S,e+1)
    i += 1
