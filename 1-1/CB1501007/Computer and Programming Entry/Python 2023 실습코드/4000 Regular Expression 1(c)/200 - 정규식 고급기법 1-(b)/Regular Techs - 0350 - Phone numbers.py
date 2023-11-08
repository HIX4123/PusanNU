
import re

book = """101-3456-8767 Phone
345-6789  010-3456-6754 510-1234 45678-9089
010-345-5678 23-5467 7777-7778 01-345-1234
110-234-567  016-567-9078 010-90 101-34f-1784
345-5675 017-34-6789  010-0000-1222
summer box
"""


phone = r'\b[1-9]\d\d-\d{4}\b'
mobile = r'\b01\d-\d{3,4}-\d{4}\b'
all = phone +"|"+ mobile
getnum = re.findall( all , book )

print("정상적인 전화번호 출력")
for x in getnum :
    print(x)


print("\n 하나의 식으로 표현하기")

xp = r'\b[1-9]\d\d-\d{4}\b|\b01\d-\d{3,4}-\d{4}\b'

getnum = re.finditer( xp , book )

for x in getnum :
    print(x.group(0))