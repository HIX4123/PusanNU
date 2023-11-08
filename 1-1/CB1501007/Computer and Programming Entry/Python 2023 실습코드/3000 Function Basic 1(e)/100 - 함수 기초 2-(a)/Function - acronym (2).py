#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-04-05
#-------------------------------------------------------------------------------


def acronym( S ) : # 파라매터
    if len(S) <= 3 : return(S)
    else :
        fchar= S[0]
        lchar=S[-1]
        mchar=S[ (len(S)-1)//2 ]
        return( fchar+mchar+lchar )

S="부산갈매기"
out = acronym(S)
print("축역어=", out)



