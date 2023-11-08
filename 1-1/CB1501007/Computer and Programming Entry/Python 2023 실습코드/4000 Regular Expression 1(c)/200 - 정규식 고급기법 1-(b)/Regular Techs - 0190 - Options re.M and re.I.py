#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


import re
p1  = re.compile(r"^python\d\s")      # 처음 시작하는 라인에서
p2  = re.compile(r"^python\d\s", re.M )  # 각 라인 시작에서
p3  = re.compile(r"python\d$", re.M|re.I )  # 각 라인 시작에서
p4  = re.compile(r"\bpython\d\s\b", re.I)

# python이라는 문자열로 시작하고 그 뒤에 whitespace,
# 그 뒤에 단어가 와야 한다는 의미이다. 검색할 문자열 data는 여러 줄로 이루어져 있다.
# 하지만 ^ 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고
# 싶은 경우도 있을 것이다. 이럴 때 사용할 수 있는 옵션이 바로
# re.MULTILINE 또는 re.M이다. 위 코드를 다음과 같이 수정해 보자.

data = """python1 one
life is too short python2
banana next word
python3 two good
python5 summer python6 ro
Where my python7 who
you need python8
  python9  Good Boy Python6"""


print( "No Options=", re.findall(p1, data))
print( "시작할 때=", p2.findall(data))
print( "끝날 때 =", p3.findall(data))
print( "word boundary=", p4.findall(data))