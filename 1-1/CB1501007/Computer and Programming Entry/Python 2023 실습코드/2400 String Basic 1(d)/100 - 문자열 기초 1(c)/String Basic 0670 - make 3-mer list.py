
ldna  = [ 'a', 'c', 'g', 't']

print("모든 가능한 3-mer 출력하기")

kmer3=[]
for p in ldna :
    for q in ldna :
        for r in ldna :
            kmer3.append(p+q+r)

for w in kmer3 :
    print(w)
