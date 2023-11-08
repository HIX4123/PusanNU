

import sys
import re
import string

def Kletter( char):
    if len(char) >=2 : return(-1)
    if( '\uAC00' <= char <= '\uD7A3' )  :   # 가 ~ 힣 : \uAC00 ~ \uD7A3
        return(1)
    else :
        return(0)

def Kjaum( char):
    if len(char) >=2 : return(-1)
    if( '\u3130' <= char <= '\u314E' )  :   # ㄱ ~ ㅎ : \u3130 ~ \u314E
        return(1)
    else :
        return(0)

def Kmoum( char):
    if len(char) >=2 : return(-1)
    if( '\u314F' <= char <= '\u3163' )  :   # ㅏ ~ ㅣ : \u314F ~ \u3163
        return(1)
    else :
        return(0)

    # 이전 코드 중 \u3130-\u318F => 옛한글을 포함합니다.
    # ㄱ ~ ㅎ : \u3130 ~ \u314E
    # ㅏ ~ ㅣ : \u314F ~ \u3163
    # 가 ~ 힣 : \uAC00 ~ \uD7A3

myk = "--- 당신은 --*1234 이것은 ab c 한글이다. ab c %^&### ㅋㅋㅋ ㅠㅠㅠ"
myl = list( myk )

for i,w in enumerate( myl) :
    print("i=", i, "char= ", w , "code=",Kletter(w), Kjaum(w), Kmoum(w))



