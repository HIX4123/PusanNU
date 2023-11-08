from functools import cmp_to_key

def myout(msg, T):
    print(f"\n >> {msg} <<")
    for w in T :
        print(w)


mem1 = ( 'Tom',      'USA  ',  51 )
mem2 = ( 'Gomez',    'USA  ',  33 )
mem3 = ( 'Smith',    'Canada', 33 )
mem4 = ( 'Beth' ,    'France', 29 )
mem5 = ( 'Samdori',  'Korea',  29 )
mem6 = ( 'Nakazima', 'USA  ',  66 )

lotte = [ mem1, mem2, mem3, mem4, mem5, mem6 ]

myout("1. 실험 전 ", lotte)

lotte.sort()
myout("2. 정렬 후 ", lotte)


def xcmp(x) :    #두번째 원소, 나이가 비교 기준
    return x[1],x[2], x[0]


# 내가 정한 기준 sort
Slotte = sorted( lotte, key = xcmp )
myout("3. 개인 정렬 후 ", lotte)
