

import re

st="들길따라서 나 홀로 걷고 싶어\
작은 가슴에 고운 꿈 새기며\
나는 한 마리 파랑새 되어\
저 푸른 하늘로 날아가고파\
사랑한 것은 너의 그림자\
지금은 사라진 사랑의 그림자\
\
물결 따라서 나 홀로 가고 싶어\
작은 가슴에 고운 꿈 안으며\
나는 한 조각 작은배되어\
저 넓은 바다로 노저어가고파\
사랑한 것은 너의그림자\
지금은 사라진 사랑의 그림자\
\
들길 따라서 나 홀로 걷고 싶어\
작은 가슴에 고운 꿈 새기며\
나는 한 마리 파랑새 되어\
저 푸른 하늘로 날아가고파 사랑한 것은\
너의 그림자 지금은 사라진 사랑의 그림자\
사랑한 것은 너의 그림자\
지금은 사라진 사랑의 그림자\
"

p1= r"홀로[ \w]+싶어"
p1= r"\w{5,}"

out = re.match( p1, st, re.M )
if out :
    print("In", out.group() )
else :
    print("None match( )" )


