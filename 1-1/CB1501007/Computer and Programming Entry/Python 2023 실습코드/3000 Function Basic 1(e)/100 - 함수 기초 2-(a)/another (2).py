

# ---- begin of swap( ) ----------
def swap(a,b) : # 두 값을 바꿈
    a,b = b,a
    return( )
# ---- end of swap( ) ------------


def lswap(L): # 입력이 list
    if len(L)<= 1 : return()
    L[0],L[1]= L[1],L[0]
    return()



X,Y=100,200
print(f' Before X,Y = {X,Y}')
swap(X,Y)
print(f' After  X,Y = {X,Y}')

My=[100,200,300, 400]
print(f' 넘기기전 My={My}')
lswap( My )
print(f' 넘긴 후  My={My}')






