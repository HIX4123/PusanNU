

import re

print(" --- 정규식에서 반복의 이해 --- ")

string0 = """
agtatcagaatttaaaacttagactctgaaatattctcattcccggctct
ctctctcttctctcttaggccgaaattacacggaccggaatttcgcggcc
gcggaattccgcctgcagaaatttctatggatatgacagttcagaaaagt
tgttgttgacagtttgtacatgggtttgacagcaggcgaaattacgctcc
cgcgaaactccggtactcgtttctcgtttcgtgtcttttcgaccttaaaa
aagactacccattccctttttttttttgcttttcaacgctggcgttcaat
cattgcatgcgtttatatgtcatgtgtcaccctaccttggtgagaaagtt
tgcgatcgtttctcgtttctcgtttctcgtttctcgtttcaccaaccgat
ggaggagcgtgccggaccgttcttttttttttaccgccggcggctccgct
ctggcaggaaggcacattcggtgttcgtttctttgtcgacgcgctggacg
gacgagggctgcggtacggtacggtccacctcaccatcctcgcccacgtc
"""


string1 = string0.replace('\n','')
print( f'string0={ len(string0)}, string1={ len(string1)}' )


print("\n 실험 10, 반복의 최소, 최대 ")
s = re.findall(r"ct{3,}", string1)
print(s)

print("\n 실험 20, findall( )에서의  반복")
s = re.findall(r"((ct){3,})", string1)
print(s)

print("\n 실험 30, finditer( )에서의 반복 ")
s = re.finditer(r"((ct){2,})", string1)
for w in s :
    print( w.span(), w.group(), "core =", w.group(2) )

print("\n 실험 40, Search( )로 반복 찾기")
s = re.search(r"(ct){2,}", string1 )
re.search
print(s)

print("\n 실험 50, finditer로 반복 찾기")
s = re.finditer( r"((tcgtttc){2,})", string1)
for w in s :
    print( w.span(), w.group(), "core =", w.group(2) )


