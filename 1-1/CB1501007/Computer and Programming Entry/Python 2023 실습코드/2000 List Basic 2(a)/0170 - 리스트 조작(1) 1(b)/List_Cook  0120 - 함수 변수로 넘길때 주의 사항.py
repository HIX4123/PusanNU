#--------------------------------------------------------
# Author:      Zoh Que
# Created:     01-02-2023
#--------------------------------------------------------


# List를 넘겨줄 경우 그 변화는 모두 List에 반영된다.

def modify(L):
    a = L.pop(0)
    L.append(a)

import copy
def modify2(L):
    X = copy.copy( L )  # 새로운 복사판을 만듬
    a = X.pop(0)
    X.append(a)


L=list("Summer")
for w in range(5):
    modify(L)
    print(L)


print("\n\n List를 copy해서 넘길 때 \n")
L=list("Winter")
for w in range(5):
    modify2(L)
    print(L)