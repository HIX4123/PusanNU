
"""
meta-character

.       모든 문자와 매칭  \.
\\      역슬래쉬 문자 자체
\d      모든 숫자와 매치됨 [0-9]
\D      숫자가 아닌 문자와 매치됨 [^0-9]
\s      화이트 스페이스 문자와 매치됨 [ \t\n\r\f\v]
\S      화이트 스페이스가 아닌 것과 매치됨 [^ \t\n\r\f\v]
\w      숫자 또는 문자와 매치됨 [a-zA-Z0-9_]
\W      숫자 또는 문자가 아닌 것과 매치됨 [^a-zA-Z0-9_]
\b      단어의 경계를 나타냄. 단어는 영문자 혹은 숫자의 연속 문자열
\B      단어의 경계가 아님을 나타냄
\A      문자열의 처음에만 일치
\Z      문자열의 끝에만 일치
"""
# x? , x를 사용하거나 안하거나  books? ={book, books}
# book\?   { book?}

import re

string = "Once th뭔가요ings, you3may _BOY safely."
string2 = "Is this reality, good.  boy who are you ? ㅎㅎㅎ,,,ㅎ뭔가요 "

# UNICODE가 아닌 문자로 자름
mlist = re.split("\W+", string)
for x in mlist:
    print("\W 단위로 잘라낸 토큰", x)

mlist = re.split("[\.,\?]", string2)
for x in mlist :
    print(" {. , ?} 단위로 잘라낸 토큰", x)

# 2개 까지만 \W로 잘라낸 문자
mlist = re.split("\W+", string, 2)
for x in mlist:
    print("첫 두개까지의 토큰: ", x)



