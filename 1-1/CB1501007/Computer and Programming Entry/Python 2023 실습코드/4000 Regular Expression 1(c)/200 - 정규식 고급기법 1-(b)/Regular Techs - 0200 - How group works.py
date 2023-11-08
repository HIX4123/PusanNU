

import re

dna = "agtcggcctcctcctcctcggatggtagacaacaacaagtcgtttagatatatagc"
txt=  'a-q+b-z-e/c-e+f-w=k'
m = re.findall( r'(?:\w[+-])+', txt )
print( m )

print( re.findall(r"(?:cct)+", dna ) )