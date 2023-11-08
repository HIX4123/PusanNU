

import re

patt01= r"[a-z]"    # a에서  z까지의 모든 문자, 소문자 1자
patt01= r"[-az]"    # 문자 -, a, z, 3문자
patt03= r"[^abcz]"  # a,b,c,z 를 제외한 모든 문자, Caret, hat
patt04= r"[ab^cz]"  # 문자 a, b, c, ^ , 또는 z
patt05= r"[A-Z]"    # A에서  A까지 대문자



s1 = "Mayer is a very common Name He is called Meyer but he isn't German."
s= re.search(r"M[ae][iy]er",  s1)
print("(1)=", s)

s= re.search(r"M[ae][iy]er",  s1)
print("(2)=", s)

s= re.match (r"M[ae][iy]er",  s1)
print("(3)=", s)

s= re.match(r"M[ae][iy]er",  s1)
print("(4)=", s)

s= re.search(r"^M[ae][iy]er", s1)
print("(5)=", s)

s= re.search(r"^M[ae][iy]er", s1)
print("(6)=", s)





