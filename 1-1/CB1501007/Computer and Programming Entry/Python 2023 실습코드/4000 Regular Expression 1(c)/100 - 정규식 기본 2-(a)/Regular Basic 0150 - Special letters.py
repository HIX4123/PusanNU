

import re

string1='''
Wednesday child is a child of woe.
Wednesday child cries alone, I know.
When you smiled, just for me you smiled,
For a while  I  forgot 3324 I was Wednesday $$  child.
Friday's child wins      at love, they say.
In your arms Friday was my day.
Now you're gone, well 5678 I # should have known,
I am Wednesday   child   born to be alone.
Now you're gone well I should have known,
I am Wednesday child, born to be alone.
Wednesday's   child born to 6896   345_900 bxxxxx alone
'''

print("특수문자를 이용한 매칭 Part2")

print("\n 실험 10, \\b문자 word boundary")
# \b는 word boundary를 검사
s = re.findall(r"\w+s\b", string1)
print( s )


#\w는 모든 알파뉴메릭 (영문자, 숫자)과 '_' 문자를 매칭, 변수문자
print("\n 실험 11, \\w 문자, 변수문자")
s = re.findall(r"\w\w\w", string1)
print( s )

#\W는 모든 알파뉴메릭과 underbar를 제외한  (영문자, 숫자) 문자를 매칭
print("\n 실험 12, \\W, non-변수문자 ")
s = re.findall(r"[\W]", string1)
print( s )

#\s는 모든 white space를 매칭
print("\n 실험 13, \\s white space의 의미 ")
s = re.findall(r"\s\s.+\s\s", string1)
print( s )


print("\n 실험 14, \\S white space가 아닌 모든 문자 ")
s = re.findall(r"(\S*\s*\S*)", string1)
print( s )


print("\n 실험 15, \\d digit chars ")
s = re.findall(r"\d+", string1)
print( s )



