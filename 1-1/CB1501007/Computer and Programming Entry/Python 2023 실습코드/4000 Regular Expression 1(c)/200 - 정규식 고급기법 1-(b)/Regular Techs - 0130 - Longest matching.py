

import re

dna = "agtcggwcctwcctcctcctcggatwggtagacaacaacaagtcgtttagatatatagc"
txt=  'a-q+b-z-e/c-e+f-w=k'

print( re.findall( r'(?:\w[+-])+\w', txt ) )

print( re.findall(r"(?:cct)+", dna ) )


print( re.findall(r"w\w+w", dna ) )