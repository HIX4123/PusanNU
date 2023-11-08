

import re

dna = "agtcggwcctwcctcctcctcctcggatwggtaaacaagtcgtttagatatatagc"
txt=  'a-q+b-z-e/c-e+f-w=k+a+o+z-e'

print( re.findall( r'(\w[+-])+\w', txt ) )  # 반복의 경우 처음 matching된 것을 돌려줌

print( re.findall( r'(?:\w[+-])+\w', txt ) ) #?:를 사용하면 longest를 찾아줌

print( r"(cct){3,} >>", re.findall( r"(cct){2,}", dna ) )
print( r"(?:cct)+ >>", re.findall(r"(?:cct)+", dna ) )


print( r"w\w+w >> ", re.findall(r"w\w+w", dna ) ) # repeat이 아닌 경우 longest