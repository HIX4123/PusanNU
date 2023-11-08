

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


chat = "술마시러 가자 ㅎㅎㅎ ㅋㅋㅋ"

count = 0
for w in chat :
    if Kjaum(w) or Kmoum(w) :
        print(w)
        count += 1

print( "잡소리 비율= ", count / len( chat ) )
if  count / len( chat ) > 0.3 :
    print( "\n 교양있는 말투를 쓰세요. ")
else :
    print("좋은 말입니다. 전달가능 ")