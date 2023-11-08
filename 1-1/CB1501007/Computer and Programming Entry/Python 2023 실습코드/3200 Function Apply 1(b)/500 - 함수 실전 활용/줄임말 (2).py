#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-24
#-------------------------------------------------------------------------------


def acron2():
    pass

def acronym( S ):
    N= len(S)
    Slist = S.split()
    ejol = len( Slist )
    if ejol == 1 :
        if N <= 6 : mys = S[0]+               S[-1]
        else :      mys = S[0]+ S[int(N/2)] + S[-1]
    if ejol == 2 :
        mys = Slist[0][0]+ Slist[1][0]+ Slist[1][-1]
    return( mys )


def foo():
    pass

T=["찰학 개론", "파이선 입문", "중앙도서관", "국립에너지연구센터",
    "대한 무기력협회", "순대국밥"]


for i,w in enumerate(T) :
    mshort = acronym(w)
    print(f"{i}, 원어= {w}, 약어={mshort}")

a=[1,2,3]









