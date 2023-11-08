

#정규식(Regular expression)을 이용하여 split하는 방법을 배웁니다.

import re
splitter = re.compile(r'[\D]') # Match non-digits
a= splitter.split("2+24*48/32=10")
print("실험 1", a)
b= re.split(r'[\D]', '2+24*48/32')
print("실험 2", b)
this = "1 2 3 4 5 "
ml = this.split()
print("실험 3", ml)