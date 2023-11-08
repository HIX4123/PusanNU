

import re

print("Greedy Matching\n")
s = '<html><head><title>Title</title>'
print(len(s))

print("\n 가장 길게 매칭")
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())
# qualifiers *?, +?, ??, or {m,n}?  match as little text

print("\n 가장 짧게 매칭")
print(re.match('<.*?>', s).group())

