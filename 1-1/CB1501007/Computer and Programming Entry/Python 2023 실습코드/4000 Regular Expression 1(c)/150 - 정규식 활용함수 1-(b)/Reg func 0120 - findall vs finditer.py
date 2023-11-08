

import re

string = "Once you have accom  plished small --+ 567 apple good th뭔가요ings, you may atte똥mpt safely."

# 'a'로 시작되는 모든 단어를 찾는다.
print(re.findall(r"\ba[\w]*", string))


# 'a'로 시작되는 모든 단어를 찾아서 그것을 iterator로 돌려준다.
it = re.finditer(r"\ba[\w]*", string)
for match in it:
    print("매칭단어=", match.group(), "매칭구간=", match.span())


# UNICODE가 아닌 문자로 자름
mlist = re.split("\W+", string)
for x in mlist:
    print("\W 단위로 잘라낸 토큰", x)


# 2개 까지만 \W로 잘라낸 문자
mlist = re.split("\W+", string, 2)
for x in mlist:
    print("첫 두개까지의 토큰: ", x)



