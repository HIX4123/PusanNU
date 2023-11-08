
import random
sa = set( [1, 2, 3] )
sb = set( [1, 2, 3, 6, 7, 8, 9, 10] )

w = random.choice(list( sa ))
print("w= ", w)


q = random.sample( sb , 4)
print("q= ", q)

a = random.sample( sb , 3)
print("a,a[0]= ", a, a[0])

lw=list("부산갈매기금정산막걸리")
kw=set(list("부산갈매기금정산막걸리"))
for w in range(10):
    mword = random.sample( kw,3)
    print(mword)

for w in range(10):
    mword = random.sample( kw,2)
    print(mword)

for w in range(10):
    mword = random.sample( lw,4)
    print(mword)

#pop 뽑아내기
#sample 추출, 복원추출