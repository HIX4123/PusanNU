
import re
string1= """Wednesday 3child is a child of woe.
Wednesday 4child cries alone, I know.
I was When you smiled,
For a while  I  9forgot 3324
I was Wed34nesday $$  child.
Friday's child wins  at love, they say.
"""

print("특수문자를 이용한 매칭 Part2")

print("\n 실험 1, \\D non-digit chars ")
s = re.findall(r"\D+", string1)
print(s)


print("\n 실험 2, \^ 입력 라인의 처음")
s = re.findall(r"^W[a-z]+", string1)
print(s)

print("\n 실험 3, \$ 입력 라인의 끝. ")
s = re.findall(r"[a-z]\.$", string1)
print(s)



print("\n 실험 4, [^\d\n\W] 숫자,줄바꿈,특수 문자가 없는 모든 단어")

s = re.findall(r"[^\d\n]+", string1) #s, t, 공백 리턴문자가 없는 단어
print(s)






