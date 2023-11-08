
# 여기를 보세요 http://www.tutorialspoint.com/python/python_reg_expressions.htm
import re

print(" raw string과 일반 string의 차이")
str1 =  "\tbanana"
str2 = r"\tbanana"  # r의 raw string, 각종 \key를 그대로 사용함
str3 =  "\bbanana" # \b는 word boundary
print(str1, str2, str3)

text = "Ban Start Xan[Bananacake banana Gpineapple Bananas :Ban this pigbanana"

p01 = "[baanna]"
p02 = "banana"
p03 = r"Banana|banana"
p04 = "[Bb]anana"
p05 = r"\bbanana\b"
p06 = r"\b[Bb]ananas?\b"


print("p01 =", re.findall( p01, text ))
print("p02 =", re.findall( p02, text ))
print("p03 =", re.findall( p03, text ))
print("p04 =", re.findall( p04, text ))
print("p05 =", re.findall( p05, text ))
print("p06 =", re.findall( p06, text ))

all1 = re.findall( r"\b(ban|Ban)", text)
all2 = re.findall(  "\b(ban|Ban)", text) # raw가 아닌 경우와 비교해보자.
all3 = re.findall(  "( ban| Ban)"  , text) # 공백이 먼저 나오는 경우
print("all1=", all1)
print("all2=", all2)
print("all3=", all3)

here = re.finditer( r"\b(ban|Ban)", text )
for posi in  enumerate(here) :
    print(posi[0]+1 , "번째 단어위치", posi[1].span())

# Token 분해하기
expr = "b = 2456 + abcd*10 - 7.8"
print(re.findall("\s*(\d+|\w+|.)", expr)) # \s는 white space = [\t\n\r\f].

# 괄호로 쳐진 순서에 따라서 그룹을 지어 돌려준다.
print("\n 3가지 매칭된 결과 ( A | B | C) 결정한다")
for item in re.findall("\s*(?:(\d+)|(\w+)|(.))", expr):
    print(item)