
# re.search( )는 re.match와 달리 모든 라인에 대하여
# 다 조사를 해준다. 중요한 것은 first occurence만 찾아줌.
# 첫번째만 찾으면 됨. 모두다 찾으면 시간이 걸림.
# 생수통이 있는가 ?

#  빨리 있는지의 여부를 확인할 때 re.search( )

import re

st="""
들길 따라서 나 홀로 걷고 싶어
작은 가슴에 고운 꿈 새기며
나는 한 마리 파랑새 되어
저 푸른 하늘로 날아가고파
사랑한 것은 너의 그림자
지금은 사라진 사랑의 그림자

물결 따라서 나 홀로 가고 싶어
작은 가슴에 고운 꿈 안으며
나는 한 조각 작은배되어
저 넓은 바다로 노저어가고파
사랑한 것은 너의그림자
지금은 사라진 사랑의 그림자

들길 따라서 나 홀로 가 고 고 싶어
작은 가슴에 고운 꿈 새기며
나는 한 마리 파랑새 되어
저 푸른 하늘로 날아가고파 사랑한 것은
너의 그림자 지금은 사라진 사랑의 그림자
사랑한 것은 너의 그림자
지금은 사라진 사랑의 그림자
"""

p1= r"홀로[  \w]+싶어"
#p1= r"\w{5,}"

out = re.search( p1, st )
if out :
    print("In", out.group(), out.span()  )
else :
    print("None match( )" )

out = re.search( p1, st[19:] )
if out :
    print("In", out.group(), out.span()  )
else :
    print("None match( )" )


out = re.finditer( p1, st)
for w in out :
    print(f'w={w.group()}, {w.span()}')




