#--------------------------------------------------------
# Author:      Zoh Que
# Created:     02-02-2023
#--------------------------------------------------------

def modil(L):
    e=L.pop(0)
    L.append(e)
    return(L)

def modil2(L):  #만일 L의 left handed 변수가 되면 이것은 Call by Value가 되고
    X=L[:]      # L에 반영이 되지 않는다.  L = 이 되는 순간 새로운 Local List가 만들어진다.
    e=X.pop(0)
    X.append(e)
    L=X[:]
    return(L)



A=list("123456")
print(A)
modil(A)
print(A)
modil(A)
print(A)
modil(A)
print(A)

A=list("789012")
print(A)
modil2(A)
print(A)
modil2(A)
print(A)
modil2(A)
print(A)

