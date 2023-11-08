
import re

text1= "agttgggaccgataattgggtatatag\
gtcggataataaaaatagtacgcgctagctataag\
atcgttaggtagaaataggcccctaggatcgaaac\
tcgggataggctagaatta"

mypat= re.compile( r"gcta[agtc]*taga")

print("특정 유전자, 시작은 gcta, 끝은 taga로 끝나는 스트링")
print(mypat.findall( text1 ))


text= "agttgggaccgataattgggtatatag\
gtctggataa(cgcgcgcgcgcg)cgcgcgttaga\
atcgttaggtagaaataggcccctaggatcgaaac\
tcgggataggcgcgcgcgccagaaagttaatta"

mypat= re.compile( r"(cg)+")

print("Repeating subsequence example")
itlist = re.finditer( mypat, text )
for no, mym in enumerate(itlist) :
    print("위치 = (%4d 부터 %4d)까지 " % mym.span(), end=' ')
    print("해당 단어= %8s" % mym.group())