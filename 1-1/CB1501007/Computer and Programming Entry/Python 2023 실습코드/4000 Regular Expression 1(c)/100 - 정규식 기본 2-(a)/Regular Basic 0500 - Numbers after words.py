
import re

text = "summer 0.325 time killer975.4 we .90 87..123 are the456 world 1234 goof12 45.67"

pat = '\d+\.?\d+'  # 숫자가 반복, 소숫점은 있어도 되고, 없어도 됨.
plist = re.findall( pat, text )

print("정식으로 바르게 표시된 숫자 묶음")
for x in plist :
    print(x)


print("\n Search()를 이용해서 문자뒤의 숫자 찾아내기")
pat = '\w+(\d+)' #문자와 숫자의 결합 중 숫자부분
plist = re.search( pat, text )
print(plist.group())


plist = re.findall( pat, text )
print(plist)