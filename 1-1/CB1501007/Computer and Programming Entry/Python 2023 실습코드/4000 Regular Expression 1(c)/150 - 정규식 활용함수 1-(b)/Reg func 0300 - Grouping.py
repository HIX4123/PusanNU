
# re.M == re.MULTILINE # 여러 라인에 걸쳐서 찾는다.
# re.I == re.IGNORECASE # 대소문자 구별하지 않는다. A와 a는 같은 것으로


import re

line = "Cats are smarter \n than dogs. Students are smarter than Professors. "

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

print("------- matching Object -------")
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")

print("------- Searching Object -------")
line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")

print("------- Matching과 Searching의 차이  -------")
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Nothing found!!")