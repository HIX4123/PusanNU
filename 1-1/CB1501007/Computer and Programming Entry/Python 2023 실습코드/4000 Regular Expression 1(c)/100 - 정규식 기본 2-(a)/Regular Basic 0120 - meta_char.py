"""
.       모든 문자 , 쩜 자체를 표시하려면 백슬래쉬를 추가  \.
\\      역슬래쉬 문자 자체
\d      모든 숫자와 매치됨 [0-9]
\D      숫자가 아닌 문자와 매치됨 [^0-9]
\s      화이트 스페이스 문자와 매치됨 [ \t\n\r\f\v]
\S      화이트 스페이스가 아닌 것과 매치됨 [^ \t\n\r\f\v]
\w      숫자 또는 문자와 매치됨 [a-zA-Z0-9_]  word(w)
\W      숫자 또는 문자가 아닌 것과 매치됨 [^a-zA-Z0-9_]
\b      단어의 경계를 나타냄. 단어는 영문자 혹은 숫자의 연속 문자열
\B      단어의 경계가 아님을 나타냄
\A      문자열의 처음에만 일치
\Z      문자열의 끝에만 일치
"""

import re
string='''
Wednesday's child is a child of woe.
Wednesday's child cries alone, I know.
When you smiled, just for me you smiled,
For a while I forgot I       was Wednesday's child.
Friday's child wins at love, they say.
In your arms Friday was my day.
Now you're gone, well I  should have known,
I am Wednesday's child, born to be alone.
Now you're gone, well I     should boooaoa have known,
I am Wednesday's child, booere to be alone.
Wednesday's child, born to bxxxxx alone
'''

# . 쩜은 아무 문자 한(single) 문자에 매칭


print("\n 실험 01, 점(.) 매칭")
s1 = re.findall(r"c...", string ) # c로 시작되는 길이 4인 문자열
print(s1)


print("\n 실험 02, 괄호의 용법")
# Groups a series of pattern elements to a single element.
s1= re.findall(r"I[ ]+[a-z]+", string ) # I 다음에 오는 단어
print("\n 괄호가 없을 때 ", s1)
s1= re.findall(r"I[ ]+([a-z]+)", string ) # I 다음에 오는 단어
print("\n 괄호가 있을 때 ",s1)

# +는 한번 이상 반복
print("\n 실험 03, '+'문자의 반복")
s1=re.findall(r"b[aeiou]+", string)
print(s1)


# ? 앞의 단일 문자를 사용하든지 말든지
print("\n 실험 04, 점이나 콤마가 끝에 붙은 단어")
s1=re.findall(r"[a-z]+[.,]", string)
print(s1)

print("\n 실험 05, 대문자로 시작하는 단어  ")
s1=re.findall(r"[A-Z][a-z]*", string)
print(s1)




