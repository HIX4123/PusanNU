import re


string1 = """
우리 교수님 독독독한 교수님은 괴수님,
월 수 쌩고생하시는 교수님님, 엉엉 만 만 세
컴시입컴시입컴시입  교짱짱수 만만세 공부해서 남주자
빨리빨리 종강해서 건강도 되찾고 교장선생님목수 놀러가야지.
교수님 안녀엉엉엉엉엉
"""

# | bar는 선택
print("\n 선택 실험 01, | 를 이용한 선택 ")

mypat = re.compile(r"\b(교수|괴수|교[가-힝]*수)\b")
s= re.findall( mypat , string1)
print(s)


print("\n 선택 실험 02,  Search를 이용한 선택 ")
s= re.search( mypat , string1)
print(s)

print("\n 선택 실험 03,  match를 이용한 선택 ")
s= re.match( mypat , string1)
print(s)

print("\n 선택 실험 04,  finditer를 이용한 선택 ")
s= re.finditer( mypat , string1)
for w in s :
    print(w.start(), w.group(), "w.group(1)=", w.group(1))