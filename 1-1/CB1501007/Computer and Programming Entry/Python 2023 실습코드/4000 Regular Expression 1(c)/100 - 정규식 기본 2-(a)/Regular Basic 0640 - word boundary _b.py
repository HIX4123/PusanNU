#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------

import re

"""
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



data = """
python1
life is too short python2
banana next PythonQ  word py
thon3 three python zpythonz
three Python4
"""
myp= r"[Pp]ython"
print( "ex01= ", re.findall( r"[Pp]ython\d", data) )
print( "ex02= ", re.findall( myp + ".", data) )
print( "ex03= ", re.findall( r"\s[Pp]ython\d\s", data) )
print( "ex04= ", re.findall( r"\b[Pp]ython\d\b", data) )