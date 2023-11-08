# Zoh 작성한 list permutation code 2023. Feb. 3
#
# 속도를 위하여 non-recursive version으로 작성함.
# 만일 일반적인 list를 사용한 경우에는 이 순서를 사용한 다음
# 해당 리스트의 원소를 다시 바꾸어야 함.
# 입력은 L=[1,2,3,...n ]이면
# nextp( L )는 이 list L의 다음 permutation 순서를 List L로 return함.
# call by reference이므로 입력 parameter L 자체가 변화됨에 주의
#
# L이 마지막 permutation인 경우 null list [ ]를 return 함.
#

import copy
import math

def end_cut(L):
    if len(L) == 0 : return(0)
    for idx in range(len(L)-1,0,-1) :
       # print(f"> idx = {idx}")
        if( L[idx-1] < L[idx]) :
            return idx
    return(0)



def check(L):
    A = set(L)
    B = set( [x for x in range(1,len(L)+1)])
    if A != B :
        return( False )
    else :
        return( True )

def nextp(L):
    if not check(L) :
        return("Index Error")

    mcut = end_cut(L)
    #print(f" L={L}, mcut={mcut}")
    if mcut == 0 : return( [] ) # 다시 처음으로 돌아옴.

    Ltop   = L[ mcut:      ]
    Lbot   = L[     :mcut-1]
    bottom = L[ mcut-1     ]
    #print(f" Ltop={Ltop}, Lbot={Lbot}, bottom={bottom}")

    Ltop.append( bottom)
    Ltop.sort()
    bindex = Ltop.index( bottom )
    enew   = Ltop.pop( bindex + 1)
    Lbot.append( enew )
    L = Lbot + Ltop
    if not check(L) : return("Index Error")

    return(L)


X=[1,2,3,4,5,6]
alln = math.factorial( len(X) ) + 1

for i in range( alln ):
    X=  nextp( X )
    print(f"i={i+1:4}, {X}")


U = [[1,2,3,6,5,4],    [1,2,3,4,5,6],[1,7,6,5,4,3,2],
      [1,2,3,6,5,4,7], [7, 6, 5, 4, 3, 2, 1],
      [5,4,3,2,6,7,1]
]
for w in U :
    print(f"L={w}, next={nextp(w)}")