#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-26
#-------------------------------------------------------------------------------


def make_2d(N,M):
    if N <= 0 or M <= 0 :
        print("size error")
        exit(0)

    U=[]
    for i in range(N) :
        T=[]
        for j in range(M):
            T.append(None)
        U.append(T)

    return(U)


S= make_2d(3,5)
S[0][3]="Good"
for w in S :
    print(w)