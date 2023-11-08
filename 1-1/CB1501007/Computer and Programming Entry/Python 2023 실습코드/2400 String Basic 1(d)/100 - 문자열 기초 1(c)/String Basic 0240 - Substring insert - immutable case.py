#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-04-08
#-------------------------------------------------------------------------------

# 불행히도 string에는 insert가 없다. immutable object이기 때문이다.
# 그래서 항상 이것에 작업을 할 경우에는 list로 바꿔야 한다.

A="this is a simple statement."


def string_insert( T, k, P):
    TL = list(T)
    if k > len(T) :
        print("Out if Index error")
        return
    TL.insert(k,P)
    F= ''.join(TL)
    return(F)


W= string_insert(A,3,"----")
print(W)

W= string_insert(A,10,"크크크")
print(W)