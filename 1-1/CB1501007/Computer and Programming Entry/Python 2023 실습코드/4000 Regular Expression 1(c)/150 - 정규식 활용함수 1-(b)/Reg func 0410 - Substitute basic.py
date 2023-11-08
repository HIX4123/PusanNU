#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
import re

string = " Summer , good day boy 010-3456-8906 , My Phone"
print("\n 특정 delimiter를 : 문자로 바꿈")
print(re.sub("[,]", ":", string))

print("\n 전화번호의 - 를 삭제한다. ")
print(re.sub("[-]", "", string))

print("\n Replace maximum 2 occurences of pattern")
print(re.sub("[ ,.]", ":", string, 2))

print("\n subn( )은  tuple (결과물, 교체횟수)를 돌려준다. ")
print( "%s에서 \n %d번 교체함)"% re.subn("[,]", "-", string))


ktxt="야 오늘 날씨 개좋은 날이구나. 오늘 개열심히 공부하자"

nt = re.sub(r"\s개[가-힝]+\s", " ?", ktxt )
print(nt)
