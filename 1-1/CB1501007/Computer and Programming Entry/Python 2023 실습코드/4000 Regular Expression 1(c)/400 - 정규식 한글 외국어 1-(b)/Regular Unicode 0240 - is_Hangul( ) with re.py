

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
    return hanCount > 0

myk = "--- 당신은 --*1234 이것은 ab c 한글이다. ab c %^&### ㅋㅋㅋ ㅠㅠㅠ"
myl = list( myk )

kword = ""
for i,w in enumerate( myl) :
    if( isHangul(w)) :
        print("i=", i, "char= ", w )
        kword += w


print("최종 정리된 word=", kword)