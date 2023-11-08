

import string

dna = "AAAGTCCGCTAAAGCATTCGAAATGCA"


print(dna.replace("G", "_"))  # 전부 다
print(dna.replace("G", "_", 2))  # 첫 2개만
print(dna.replace("G", "_", 7))  # 첫 7개만


