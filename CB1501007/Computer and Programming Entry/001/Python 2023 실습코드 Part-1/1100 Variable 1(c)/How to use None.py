#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
# Created:     16-03-2022
#-------------------------------------------------------------------------------
N=5
Dlist=[ [ None for w in range(N)] for q in range(N)]

Dlist[3][3]="-900"
print(Dlist)

Mdic={}
Mdic["하나"]=1
Mdic["둘"]=2
Mdic["셋"]=3
Mdic["넷"]=4

print( Mdic["둘"])
#print( Mdic["다섯"]) # 이렇게 하면 error
print( Mdic.get("다섯"))


def foo(a,b):
    z=a+b  #돌려주는 것이 없을 때 None이 자동

def nadd(a,b=None):
    if b == None :
        return a*a
    else :
        return a+b



print( foo(3,5))
print( nadd(10))
print( nadd(10, 20))