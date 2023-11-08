
import re


text = """
gcggaattccgcctgcagaaatttctatggatatgacagttcagaaaagt
tgttgttgacagtttgtacatgggtttgacagcaggcgaaattacgctcc
cgcgaaactccggtacgtgtcttttcgaccttaaaatactcacggaccaa
aagactacccattccctactctcttcttttacccaacgctggcgttcaat
cattgcatgcgtttatatgtcatgtgtcaccctaccttggtgagaaagtt
tgcgatcgtttcaccaaccgatcgtccacgaccgagccctcctcgatggt
ggaggagcgtgccggaccgttcgggtcggggaaccgccggcggctccgct
"""


print("입력 텍스트의 길이=", len( text))

mypat = "(at|ag)[agtc]*?(tt|gg)"  # at나 ag로 시작하고 끝이 tt,aa로 끝남

itlist = re.finditer( mypat, text )

for no, mym in enumerate(itlist) :
    print("위치 = (%4d 부터 %4d)까지 " % mym.span(), end=' ')
    print("mym.group( ) = ", mym.group(0),mym.group(1),mym.group(2))

