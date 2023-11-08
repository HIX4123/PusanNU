from functools import cmp_to_key

mem1 = ( 'Tom',      'USA  ',  51 )
mem2 = ( 'Gomez',    'USA  ',  33 )
mem3 = ( 'Smith',    'Canada', 33 )
mem4 = ( 'Beth' ,    'France', 29 )
mem5 = ( 'Samdori',  'Korea',  29 )
mem6 = ( 'Nakazima', 'USA  ',  66 )

lotte = [ mem1, mem2, mem3, mem4, mem5, mem6 ]

print("\n 실험 1: 정렬 전 ")
for w in lotte :
    print(w)

lotte.sort()
print("\n 실험 2: 정렬 후 ")
for w in lotte :
    print(w)


def xcmp(x) :    #두번째 원소, 나이가 비교 기준
    return x[1],x[2], x[0]
    # return x[2],x[1], x[0]
#Slotte = sorted( lotte, key = cmp_to_key(mycmp))    # 내가 정한 기준 sort
Slotte = sorted( lotte, key = xcmp )

print("\n 실험 3")
for w in Slotte :
    print(w)