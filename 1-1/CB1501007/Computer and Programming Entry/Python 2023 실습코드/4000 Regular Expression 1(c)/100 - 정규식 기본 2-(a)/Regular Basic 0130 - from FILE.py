"""
.       모든 문자  \.
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

import re

f = open('mytext.txt', 'r')

out = re.finditer(r'\b\w+ed\b', f.read())
for w in out :
    print(f'w = {w.group():15}, {w.span()}')

f.close()

f = open('mytext.txt', 'r')
out = re.finditer(r'\b\w+ing\b', f.read())
for w in out :
    print(f'w = {w.group():15}, {w.span()}')

f.close()