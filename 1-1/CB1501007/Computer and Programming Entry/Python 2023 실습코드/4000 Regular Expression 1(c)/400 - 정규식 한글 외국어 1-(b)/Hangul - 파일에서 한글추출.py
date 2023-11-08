

import sys
import re
import string

fin = open("sample.txt", "r")

def isHangul(text):
    pyVer3 =  sys.version_info >= (3, 0)
    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not str:
            encText = text.decode('utf-8')
        else:
            encText = text

    #hanCount = len(re.findall(u'[\u3130-\u3163\uAC00-\uD7A3]+', encText))
    hanCount = len(re.findall(u'[\uAC00-\uD7A3 ]+', encText))
    # 이전 코드 중 \u3130-\u318F => 옛한글을 포함합니다.
    # ㄱ ~ ㅎ : \u3130 ~ \u314E
    # ㅏ ~ ㅣ : \u314F ~ \u3163
    # 가 ~ 힣 : \uAC00 ~ \uD7A3
    if hanCount >= 1 : return(1)
    else : return(0)

def TakeKorean( S ) :
    L = list( S )
    kword=""
    for w in L :
        if( isHangul(w)) :
            kword += w

    return(kword)

line = fin.readline()
c = 0

while line:
    KW = TakeKorean(line)
    line = fin.readline()
    print(c, "=", KW)
    c+= 1

