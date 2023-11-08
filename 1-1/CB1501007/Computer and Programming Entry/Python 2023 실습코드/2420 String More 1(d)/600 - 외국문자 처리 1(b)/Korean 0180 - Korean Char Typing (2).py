# 홍정민이 수정함

import sys
import re
import string

def Ktype( w ) :
    if u'\u314F' <= w <=  u'\u3163' :
        return( "모음" )
    if u'\u3130' <= w <=  u'\u314E' :
        return( "자음" )
    if u'\uAC00' <= w <=  u'\uD7A3' :
        return( "음절" )


def isHangul(text):

    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    # 이전 코드 중 \u3130-\u318F => 옛한글을 포함합니다.
    # ㄱ ~ ㅎ : \u3130 ~ \u314E : 자음
    # ㅏ ~ ㅣ : \u314F ~ \u3163 : 모음
    # 가 ~ 힣 : \uAC00 ~ \uD7A3 : 모든 한글 음절
    return hanCount > 0

myk = "이것은 ab c 한글이다. ㅋㅋㅋ ㅠㅠㅠ"
myl = list( myk )

kword = ""
for i,w in enumerate( myl) :
    if( isHangul(w)) :
        print( f'i={i:2} char= {w}, {Ktype(w)}' )
        kword += w



print("\n 종 정리된 word=", kword)