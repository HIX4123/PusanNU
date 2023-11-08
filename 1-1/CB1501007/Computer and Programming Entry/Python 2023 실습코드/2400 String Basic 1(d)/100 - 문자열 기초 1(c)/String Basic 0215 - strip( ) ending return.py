
# string을 다양하게 분리해 본다.
# 어절을 잘라내는 기능을 한다.
# a.strip() →   문자열 a의 양쪽 공백을 모두 지운다.
# a.lstrip() →  문자열 a의 왼쪽 공백을 모두 지운다.
# a.rstrip() →  문자열 a의 오른쪽 공백을 모두 지운다.
# a.replace(s, r) → 문자열 a의 s라는 문자열을 r이라는 문자열로 치환한다.
# a.split(s) →  문자열 a를 s를 구분자로 하여 나누어 준다. a.split()은 공백을 기준으로 한다. 이때 s는 제외된다.



wstr="\n\nSummer Time\n"

lstr= wstr.rstrip()

mstr = lstr.split('|')
print("result=", lstr)

cinema="우리는 간다/김달수/오정혜/쓰릴러/부산국제영화제"

L = cinema.split("/")
print(L)

