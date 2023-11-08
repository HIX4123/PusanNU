"""
\b Returns a match where the specified characters are at
the beginning or at the end of a word

\s Returns a match where the string contains a white space character

\S Returns a match where the string DOES NOT contain a white space character

"""

import re

string='''
Halfway through the Democratic  presidential Debate in Detroit
on Tuesday night, there was an illuminating
exchange between
Senator Elizabeth Warren, who consistently
solutions, Not Not
'''

# 대문자로 시작하는 단어를 모두 찾는다.

# boundary \b
# white string \s

s1 = re.findall(r"\b[A-Z]\w+\b", string ) # blank는 결과에 불포함
print(r"\b\w+\b = ", s1)

print("\n \\b[A-Z]\\w+\\b로 찾을 경우 ---- " )
for w in s1 :
    print(f' w = {w}')


s1 = re.findall(r"\s[A-Z]\w+\s", string ) # \s는 결과에 포함
print("\n", r"\s[A-Z]\w+\s로 찾을 경우 ---- " )
for w in s1 :
    print(f' w = {w}')




