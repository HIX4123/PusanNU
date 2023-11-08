#
# 2020 컴퓨터 입문

import sys
import re
import string

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
    # ㄱ ~ ㅎ : \u3130 ~ \u314E
    # ㅏ ~ ㅣ : \u314F ~ \u3163
    # 가 ~ 힣 : \uAC00 ~ \uD7A3
    return hanCount > 0

myk = "이것은 ab c 한글이다. 大器晩成 ㅋㅋㅋ ㅠㅠㅠ"
myl = list( myk )

kword = ""
for i,w in enumerate( myl) :
    if( isHangul(w)) :
        print("i=", i, "char= ", w )
        kword += w


print("최종 정리된 word=", kword)