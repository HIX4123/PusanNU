
# Purpose: 정규식에서 그룹 찾아내기



import re
print("\n\n 실험 1 - group의 깊이")
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print(m.group(0))  #가장 큰 그룹
print(m.group(1))
print(m.group(2))


print("\n\n 실험 3")
woo = r'(([0-9]+)-[0-9]+)-[0-9]+' #여는 괄호 순서에 따라 group이 생성됨
line = "345-677-3829"

xxx = re.match( woo, line )
if xxx :
    print(xxx.group(0))
    print(xxx.group(1))
    print(xxx.group(2))

print("\n\n 실험 4")
line = "Cats are smarter than dogs";

matchObj = re.match( r'(.*) are (\w*)', line, re.M|re.I)

if matchObj:
   print("matchObj.group(0) : ", matchObj.group(0))
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
