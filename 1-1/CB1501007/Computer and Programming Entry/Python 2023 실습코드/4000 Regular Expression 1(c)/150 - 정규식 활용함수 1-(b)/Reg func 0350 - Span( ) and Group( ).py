

import re

text = "Here PythonX Ruby rubby Pythones cats pythoned rubbyed python. ended"
mypat = re.compile( r'python..|Python?')
m01 = re.match ( mypat, text )
m02 = re.search( mypat, text )

if m02 :
    print("group()",  m02.group())  #일치된 문자열 반환 group()
    print("start()",  m02.start())  # 일치된 첫 위치
    print("end()",    m02.end())    # 일치된 끝 위치
    print("span()",   m02.span())   # 일치된 구간
# print m01  # 이상한 것이 찍혀 나올 것이다. 그것은 저장된 pattern form

# 해당되는 패턴 전부 다 찾아보는 두 가지 방법
print(mypat.findall( text ))
olist = re.findall( mypat, text )
print(olist)


print("각 위치를 모두 찍어보기")

itlist = re.finditer( mypat, text )
for mym in itlist :
    print("한개 갑니다.", end=' ')
    print("위치 = ", mym.span(), end=' ')
    print("해당 단어", mym.group())


