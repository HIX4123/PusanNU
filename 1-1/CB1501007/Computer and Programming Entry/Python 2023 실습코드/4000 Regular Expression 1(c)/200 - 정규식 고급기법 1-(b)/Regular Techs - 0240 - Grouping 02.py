

import re

p = re.compile('(ab)*')
print("실험 01", p.match('ababababab').span())


print("\n 실험 02")
p = re.compile('(a)b')
m = p.match('ab')
print(m.group())
print(m.group(0))

print("\n 실험 03")
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print("(0)", m.group(0))
print("(1)", m.group(1))
print("(2)", m.group(2))
print("group()", m.group(2,1,2))
print("groups()", m.groups())

print("\n 실험 04: 바로 중복되는 나타난 단어")
# \1은 앞에서 matching된 단어를 이어받음
p = re.compile(r'(\b\w+)\s+\1')
print( p.search('Paris in the the spring').group() )


print("\n 실험 05: Non-capturing 1")
m = re.match("([abc])+", "abc")
print(m.groups())
m = re.match("(?:[abc])+", "abc")
print(m.groups())

print("\n 실험 06: Non-capturing 2")
p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search( '(((( Lots of punctuation )))' )
print(m.group('word'))
print(m.group(1))
