
# Purpose: 가장 긴 매칭과 짧은 매칭
# 기본은 longest
# +,*는 가장 긴 매칭을 선택
# 그러나 +? *?는 가장 짧은 매칭은 선택

import re

text = "{ 1 2 3 4 { 5 6 7 } { 9 10 11 } } 12 13 } "

paren01 = r'(\{(.+)\})' # { }로 구성된 괄호 문장 regular pattern

result = re.findall( paren01, text)
print("\n", r"-----r'\{(.+)\}'룰 사용한 경우------","\n")
print( re.match( paren01, text).group() )



#result = re.sub( paren01,  r'==>\1<==', text)
paren02 = r'(\{(.+?)\})'
print("\n", r"-----r'(\{(.+?)\})'룰 사용한 경우------","\n")
result = re.findall( paren02, text)
print( re.match( paren02, text).group() )


s = '<html><head><title>Title</title>'
print(len(s))

print("\n 가장 길게 매칭")
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
# qualifiers *?, +?, ??, or {m,n}?  match as little text

print("\n 가장 짧게 매칭")
print(re.match('<.*?>', s).group())
