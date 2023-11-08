
import re

web = r'(http://)?(www\.)?python(\.org)?'  #  이것은 정규식 표현의 예
text = '''
         this is a http://www.pusan.ac.kr or  http://www.python
         or other test form http://www.pusan.ac.kr some times
         www.python.org but quick.python.org we can find http://python.org
         '''

reweb = re.compile( web )

pattobj = re.search( web, text)

if pattobj :
    print("우리가 찾은 패턴 =>", pattobj.group())
    print("패턴의 시작 위치 =>", pattobj.start())

allcases = re.findall( web , text)
print("모든 경우=", allcases)