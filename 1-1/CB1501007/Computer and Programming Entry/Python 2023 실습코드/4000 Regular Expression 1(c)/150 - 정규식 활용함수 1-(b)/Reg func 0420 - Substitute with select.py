
# Purpose: 정규식을 이용해서 찾아서 대치하기 (Search and Replace)

import re


phone = "2004-959-559 #This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)  #전체 문장에서 Comment part를 지운다.
print("설명문이 지워진 결과 : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("숫자뿐인 Phone Num : ", num)


Korean = "부산대학교 공과대학 2034 정보컴퓨터 공학부 010-4567-3456"
myko = re.sub(r'\D', "", Korean ) # 숫자를 모두 지움
ruru = re.sub(r'교.*$', "", Korean ) # 교 뒤를 모두 지움
print("숫자를 지움 : ", myko)
print("교 글자 뒤를 모두 지움 한글 : ", ruru)


print("반복된 U나 V를 따로 표시하는 방법")
# \n은 앞에서 n번째 match된 결과를 지시하는 것이다.
spec = re.sub(r'(U|V)+', r'==>\1<==', "THIS is UUUU filter Valuve and U ?");
print(spec)
